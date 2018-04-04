# -*- codding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test_del_new'))
    old_groups = app.group.get_group_list()
    int_index = randrange(len(old_groups))
    app.group.delete_group_by_index(int_index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[int_index:int_index +1] = []
    assert old_groups == new_groups