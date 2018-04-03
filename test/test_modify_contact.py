# -*- codding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    #ToDo - ?: add precondition
    old_contact_list = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname='first_name_modified'))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)

