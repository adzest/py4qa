# -*- codding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name='test_del_fn'))
    app.contact.delete_first_contact()
