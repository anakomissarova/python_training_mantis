import random
from model.project import Project


def test_del_random_project(app, db):
    old_list = db.get_projects_list()
    if old_list:
        del_project = random.choice(old_list)
        old_list.remove(del_project)
    else:
        del_project = Project(name='tmp')
        app.project.add_project(del_project)
    app.project.delete_project_by_name(del_project.name)
    new_list = db.get_projects_list()
    assert sorted(old_list, key=lambda p: p.name) == sorted(new_list, key=lambda p: p.name)
