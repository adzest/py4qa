# -*- codding: utf-8 -*-
from random import randrange

from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='first_name_for_deletion'))
    old_contacts = app.contact.get_contact_list()
    int_index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(int_index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[int_index:int_index + 1] = []
    assert old_contacts == new_contacts
