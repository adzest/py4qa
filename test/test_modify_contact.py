# -*- codding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    #ToDo - ?: add precondition
    app.group.modify_first_contact(Contact(first_name='modified_fn'))
