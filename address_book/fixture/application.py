from selenium.webdriver.webdriver import WebDriver
from fixture.session import SessionHelper

class app(self):

    def  __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/addressbook/')


    def destroy(self):
        self.wd.quit()