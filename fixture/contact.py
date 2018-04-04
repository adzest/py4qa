from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from model.contact import Contact


class ContactHelper:
    contact_cache = None

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
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value('firstname', contact.firstname)
        # ToDo - ?: add fields filling for whole instance.

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        # submit deletion #content > form:nth-child(10) > div:nth-child(8) > input[type="button"]
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        self.accept_if_alert_present()
        self.go_to_home_page()
        self.contact_cache = None

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

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name('selected[]')[index].click()

    def go_to_home_page(self):
        wd = self.app.wd
        try:
            wd.find_element_by_link_text('home page').click()
        except NoSuchElementException:
            wd.find_element_by_link_text('home').click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        # open modification form
        self.edit_contact_by_index(index)
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name('update').click()
        self.go_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name('selected[]'))

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath('//tr[@name="entry"]'):
                str_id = element.find_element_by_name('selected[]').get_attribute('value')
                self.contact_cache.append(Contact(id=str_id))
        return list(self.contact_cache)

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        contact_row = wd.find_elements_by_xpath('//tr[@name="entry"]')[index]
        contact_row.find_element_by_xpath('//img[@title="Edit"]').click()
