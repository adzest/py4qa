# -*- codding: utf-8 -*-
from model.group import Group
from random import randrange

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test_mod_new'))
    old_groups = app.group.get_group_list()
    int_index = randrange(len(old_groups))
    group = Group(name='name_mod')
    group.id = old_groups[int_index].id
    app.group.modify_group_by_index(int_index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == app.group.count()
    old_groups[int_index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_name(app):
#        app.group.create(Group(name='test_mod_new'))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header='header_mod'))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
