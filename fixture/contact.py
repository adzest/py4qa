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
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact form
        self.change_field_value('firstname', contact.firstname)
        self.change_field_value('group_header', contact.header)
        self.change_field_value('group_footer', contact.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.select_first_group()
        # submit deletion
        wd.find_element_by_name('delete').click()
        self.return_to_home_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name('selected[]').click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('home page').click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name('edit').click()
        # fill group form
        self.fill_contact_form(new_group_data)
        # submit modification
        wd.find_element_by_name('update').click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.open_add_new_contact_page()
        return len(wd.find_elements_by_name('selected[]'))
