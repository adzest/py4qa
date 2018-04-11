import re

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
        if contact.firstname is not None:
            self.change_field_value('firstname', contact.firstname)
        if  contact.middlename is not None:
            self.change_field_value('middlename', contact.middlename)
        if contact.lastname is not None:
            self.change_field_value('lastname', contact.lastname)
        if contact.homephone is not None:
           self.change_field_value('home', contact.homephone)
        if contact.mobilephone is not None:
            self.change_field_value('mobile', contact.mobilephone)
        if contact.workphone is not None:
            self.change_field_value('work', contact.workphone)
        if contact.phone2 is not None:
            self.change_field_value('phone2', contact.phone2)
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
        self.open_contact_edit_by_index(index)
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
            for row in wd.find_elements_by_name('entry'):
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(firstname=firstname, lastname=lastname, id=id, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value')
        phone2 = wd.find_element_by_name('phone2').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, phone2=phone2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        content = wd.find_element_by_id('content').text
        if self.phones_are_present(content):
            all_phones = content.splitlines(content)[1]
        else:
            all_phones = None
        # homephone = re.search("H: (.*)", text).group(1)
        # mobilephone = re.search("M: (.*)", text).group(1)
        # workphone = re.search("W: (.*)", text).group(1)
        # phone2 = re.search("P: (.*)", text).group(1)
        return Contact(all_phones_from_view_page=all_phones)

    def phones_are_present(self, content):
        blocks = content.splitlines()
        print(blocks[1])
        if blocks[1] != u'':
            return True
        else:
            False
