from selenium.webdriver.common.by import By


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "i.fa-gears").click()
        wd.find_element(By.LINK_TEXT, "Управление проектами").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "a.navbar-brand").click()

    def add_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element(By.CSS_SELECTOR, "[name=manage_proj_create_page_token] + button").click()
        if project.name:
            wd.find_element(By.ID, "project-name").send_keys(project.name)
        if project.descr:
            wd.find_element(By.ID, "project-description").send_keys(project.descr)
        wd.find_element(By.CSS_SELECTOR, "input[value='Добавить проект']").click()
        self.open_home_page()

    def delete_project_by_name(self, project_name):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element(By.LINK_TEXT, project_name).click()
        wd.find_element(By.CSS_SELECTOR, "input[value='Удалить проект']").click() # delete project
        wd.find_element(By.CSS_SELECTOR, "input[value='Удалить проект']").click() # submit deletion
        wd.find_element(By.CSS_SELECTOR, "[name=manage_proj_create_page_token] + button") # wait return to projects page
        self.open_home_page()
