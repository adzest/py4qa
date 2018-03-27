# -*- codding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    #ToDo - ?: add precondition
    app.group.modify_first_group(Group(name='modified_'))


