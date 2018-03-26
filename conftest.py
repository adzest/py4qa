import pytest

__author__ = 'oleksi.isakov'

from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
