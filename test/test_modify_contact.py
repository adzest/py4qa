# -*- codding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_name(app):
    #ToDo - ?: add precondition
    app.contact.modify_first_contact(Contact(firstname='first_name_modified'))
