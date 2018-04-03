# -*- codding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='first_name_for_deletion'))
    old_contact_list = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)

