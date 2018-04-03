class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, photo=None, homephone=None, mobilephone=None, workphone=None, fax=None, email=None,
                 email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None,
                 ayear=None, address2=None, text=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.photo = photo  # file path
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday  # Select intl
        self.bmonth = bmonth  # Select str
        self.byear = byear
        self.aday = aday  # Select int
        self.amonth = amonth  # Select str
        self.ayear = ayear
        # Secondary section
        self.address2 = address2
        self.text = text
        self.notes = notes
