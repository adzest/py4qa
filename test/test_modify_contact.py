# -*- codding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='name_mod_new'))
    old_contacts = app.contact.get_contact_list()
    int_index = randrange(len(old_contacts))
    contact = Contact(firstname='first_name_modified')
    contact.id = old_contacts[int_index].id
    app.contact.modify_contact_by_index(int_index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[int_index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
