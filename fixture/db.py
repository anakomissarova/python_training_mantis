import pymysql.cursors
from model.project import Project


class DbFixture:

    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=dbname,
                                          user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_projects_list(self):
        projects_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("select id, name, description from mantis_project_table")
            for row in cursor:
                project_id, name, descr = row
                projects_list.append(Project(project_id=str(project_id), name=name, descr=descr))
        return projects_list
