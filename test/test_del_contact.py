# -*- codding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='first_name_for_deletion'))
    app.contact.delete_first_contact()
