from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, user, password):
        client = Client("http://192.168.64.2/mantisbt/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(user, password)
            return True
        except WebFault:
            return False

    def get_projects_list_for_user(self, user, password):
        client = Client("http://192.168.64.2/mantisbt/api/soap/mantisconnect.php?wsdl")
        try:
            soap_projects = client.service.mc_projects_get_user_accessible(user, password)
        except WebFault:
            return None
        projects = [Project(project_id=x.id, name=x.name, descr=x.description) for x in soap_projects]
        return projects
