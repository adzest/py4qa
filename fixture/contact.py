from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('add new').click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name('submit').click()
        self.go_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value('firstname', contact.firstname)
        # ToDo - ?: add filds filling for whole instance.

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath('//div/input[@value="Delete"]').click()
        self.accept_if_alert_present()
        self.go_to_home_page()

    def accept_if_alert_present(self):
        wd = self.app.wd
        try:
            WebDriverWait(wd, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

            alert = wd.switch_to.alert
            alert.accept()
            print('alert accepted')
        except TimeoutException:
            print ('no alert')

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def go_to_home_page(self):
        wd = self.app.wd
        try:
            wd.find_element_by_link_text('home page').click()
        except NoSuchElementException:
            wd.find_element_by_link_text('home').click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_xpath('//a[@href="edit.php?id=13"]').click()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name('update').click()
        self.go_to_home_page()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))
