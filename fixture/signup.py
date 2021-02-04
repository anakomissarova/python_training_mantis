from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re


class SignUpHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, user, email, password):
        wd = self.app.wd
        wd.get(self.app.base_url + "signup_page.php")
        wd.find_element(By.NAME, "username").send_keys(user)
        wd.find_element(By.NAME, "email").send_keys(email)
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        mail = self.app.mail.get_mail_text(user, password,
                                           '=?utf-8?B?W01hbnRpc0JUXSDQoNC10LPQuNGB0YLRgNCw0YbQuNGPINGD0YfRkdGC0L0=? =?utf-8?B?0L7QuSDQt9Cw0L/QuNGB0Lg=?')
        url = self.extract_confirm_url(mail)
        wd.get(url)
        wd.find_element(By.NAME, "realname").send_keys(user)
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.NAME, "password_confirm").send_keys(password + Keys.ENTER)

    def extract_confirm_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)
