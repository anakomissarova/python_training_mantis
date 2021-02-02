from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.NAME, "username").send_keys(username + Keys.ENTER)
        wd.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "span.user-info").click()
        wd.find_element(By.CSS_SELECTOR, "a[href={}]".format(self.app.base_url))
        wd.find_element(By.NAME, "username")

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.PARTIAL_LINK_TEXT, "account_page.php")) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, "span.user-info").text

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()