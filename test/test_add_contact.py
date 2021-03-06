# -*- codding: utf-8 -*-
import pytest

from data.add_contact import testdata as testdata
from model.contact import Contact


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     old_contact_list = app.contact.get_contact_list()
#     app.contact.create(Contact(firstname=''))
#     new_contact_list = app.contact.get_contact_list()
#     assert len(old_contact_list) + 1 == len(new_contact_list)
