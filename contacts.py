class Contact:
	def __init__(self,name,phone_number,email,website):
		self.name=name
		self.phone_number=phone_number
		self.email=email
		self.website=website

		
	def create_contact(self):
		self.name=input("Enter contact name")
		self.phone=input("Enter phone number")
		self.email=input("Enter email address")
		self.website=input("Enter website address")

derrick=Contact("", "", "", "")
derrick.create_contact()