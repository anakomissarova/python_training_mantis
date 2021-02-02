from selenium.webdriver.common.by import By


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "ul.nav-list li:nth-of-type(7)").click()
        wd.find_element(By.LINK_TEXT, "Управление проектами").click()
        wd.find_element(By.CSS_SELECTOR, "[name=manage_proj_create_page_token] + button").click()
        if project.name:
            wd.find_element(By.ID, "project-name").send_keys(project.name)
        if project.descr:
            wd.find_element(By.ID, "project-description").send_keys(project.descr)
        wd.find_element(By.CSS_SELECTOR, "input[value='Добавить проект']").click()
        wd.find_element(By.CSS_SELECTOR, "a.navbar-brand").click()
