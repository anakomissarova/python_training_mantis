import random
from string import ascii_letters, digits, punctuation
from model.project import Project


def test_add_project(app, db):
    old_list = db.get_projects_list()
    new_project = Project(name=''.join(random.choices(ascii_letters+digits, k=10)),
                          descr=''.join(random.choices(ascii_letters+digits+punctuation, k=25)))
    app.project.add_project(new_project)
    old_list.append(new_project)
    new_list = db.get_projects_list()
    assert sorted(old_list, key=lambda p: p.name) == sorted(new_list, key=lambda p: p.name)
