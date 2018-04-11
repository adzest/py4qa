# -*- coding: utf-8 -*-
import random
import string
from model.contact import Contact


"""
Contact(firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None, photo=None,
                 all_phones_from_home_page=None, all_phones_from_view_page=None, homephone=None, mobilephone=None,
                 workphone=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 address2=None, phone2=None, notes=None)
"""

constant = [
    Contact(firstname="f_n", middlename="m_n", lastname="l_n", homephone="+38", mobilephone="+(38097)",
            workphone="+0--1-1", phone2="+098   98"),
    Contact(firstname="", middlename="", lastname="", homephone="", mobilephone="", workphone="", phone2="")
]


def random_string(prefix, maxlen):
    if prefix != "":
        symbols = string.ascii_letters + string.digits + string.punctuation + " " * 15
    elif prefix == "":
        symbols = string.digits + " +-()[]"
    else:
        raise ValueError('Unrecognized value of ' + prefix + " due to data generation")
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, homephone=homephone, mobilephone=mobilephone,
            workphone=workphone, phone2=phone2)
    for firstname in ['', random_string('fn', 20)]
    for middlename in ['', random_string('mn', 20)]
    for lastname in ['', random_string('fn', 20)]
    for homephone in ['', random_string('', 10)]
    for mobilephone in ['', random_string('', 10)]
    for workphone in ['', random_string('', 10)]
    for phone2 in ['', random_string('', 10)]
]
