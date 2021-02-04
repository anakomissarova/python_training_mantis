import random
from model.project import Project


def test_del_random_project(app, db):
    old_list = app.soap.get_projects_list_for_user(app.admin_username, app.admin_password)
    if old_list:
        del_project = random.choice(old_list)
        old_list.remove(del_project)
    else:
        del_project = Project(name='tmp')
        app.project.add_project(del_project)
    app.project.delete_project_by_name(del_project.name)
    new_list = app.soap.get_projects_list_for_user(app.admin_username, app.admin_password)
    assert sorted(old_list, key=lambda p: p.name) == sorted(new_list, key=lambda p: p.name)
