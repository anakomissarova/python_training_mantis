import poplib
import email
import quopri
from time import sleep


class MailHelper:

    def __init__(self, app):
        self.app = app

    def get_mail_text(self, user, password, subject):
        for i in range(5):
            pop = poplib.POP3(self.app.config['james']['host'])
            pop.user(user)
            pop.pass_(password)
            num = pop.stat()[0]
            if num > 0:
                for n in range(num):
                    msglines_b = pop.retr(n+1)[1]  # message lines (bytes, quoted-printable)
                    msgtext_b = b"\n".join(msglines_b)  # message lines all together (bytes, quoted printable)
                    msgtext = quopri.decodestring(msgtext_b).decode()  # decoded message text
                    msg = email.message_from_string(msgtext)
                    if msg.get("Subject").startswith(subject):  # startswith because Subject is for some reason
                        pop.dele(n+1)                           # gets stuck together with Message-ID
                        pop.quit()
                        payload = msg.get_payload()
                        return payload
                pop.quit()
                sleep(3)
            return None
