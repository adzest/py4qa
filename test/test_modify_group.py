# -*- codding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    #ToDo - ?: add precondition
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name='modified_'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


