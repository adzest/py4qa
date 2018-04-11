# -*- coding: utf-8 -*-
import random
import string

from model.group import Group

constant = [
    Group(name="name1", header='header1', footer="footer1"),
    Group(name="", header='', footer="")

]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 15
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ['', random_string('name', 20)]
    for header in ['', random_string('header', 20)]
    for footer in ['', random_string('footer', 20)]
]
