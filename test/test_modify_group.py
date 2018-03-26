# -*- codding: utf-8 -*-
from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name='modified_'))

def test_modify_group_header(app):
    app.group.modify_first_group(Group(header='modified_'))

def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer='modified_'))
