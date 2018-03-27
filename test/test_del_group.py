# -*- codding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test_del_new'))
    app.group.delete_first_group()
