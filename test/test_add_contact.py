# -*- codding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname='first_name'))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname=''))
