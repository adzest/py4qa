__author__ = 'oleksi.isakov'


@pytest.fixture(scope = 'session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
