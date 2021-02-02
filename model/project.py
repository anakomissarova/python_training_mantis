class Project:

    def __init__(self, project_id=None, name=None, descr=None):
        self.project_id = project_id
        self.name = name
        self.descr = descr

    def __repr__(self):
        return "Project(id={}, name={}, descr={})".format(self.project_id, self.name, self.descr)

    def __eq__(self, other):
        return (self.project_id == other.project_id or self.project_id is None or other.project_id is None) and \
               self.name == other.name and self.descr == other.descr
