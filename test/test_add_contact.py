# -*- codding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name='test_fn'))


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name=''))
