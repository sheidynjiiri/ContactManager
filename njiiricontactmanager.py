class Contact:
    def __init__(self,name,phone_number,email,bday,linkedin):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.bday = bday
        self.linkedin = linkedin

    def __repr__(self):
        return """
        Name:       {}
        Number:     {}
        Email:      {}
        Birthday:   {}
        LinkedIn:   {}

        """.format(self.name, self.phone_number, self.email, self.bday, self.linkedin)

class ContactManager:
    def __init__(self, contacts=[]):
        self.contacts = contacts

    def __repr__(self):
        return '{} contacts'.format(len(self.contacts))

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
            return contacts
            return None

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)


Phone_Book = ContactManager()
Phone_Book.add_contact(Contact("Njiiri","0201415048","gathigia.njiiri@meltwater.org","200793","gathigianjiiri"))
Phone_Book.add_contact(Contact("Dennis","0700158458","dennistech@gmail.com","231089","dennistech"))
print(Phone_Book)

Phone_Book.display_contacts()






