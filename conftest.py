import json
import os.path

import pytest

__author__ = 'oleksi.isakov'

from fixture.application import Application

fixture = None
target = None


@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if (fixture is None) or (not fixture.is_valid()):
        fixture = Application(browser=browser, base_url=target["baseUrl"])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')


def pytest_configure(config):
    terminal = config.pluginmanager.getplugin('terminal')
    BaseReporter = terminal.TerminalReporter

    class QuietReporter(BaseReporter):
        def __init__(self, *args, **kwargs):
            BaseReporter.__init__(self, *args, **kwargs)
            self.verbosity = 0
            self.showlongtestinfo = self.showfspath = False

    terminal.TerminalReporter = QuietReporter
