class Contact:
	def __init__(self,name,phone_number,email):
		self.name=name
		self.phone=phone_number
		self.email=email

	def Njiiri(self):
		self.name="Njiiri"
	def Ndungu(self):
		self.name="Ndungu"

	def phone_number_(self):
		self.phone_number="0201415048"

	def email_(self):
		self.email=("sheidynjiiri@gmail.com")

Njiiri_contact=Contact("Njiiri", "0201415048", "sheidynjiiri@gmail.com")
Ndungu_contact=Contact("Ndungu", "0726946002", "dennisttech@gmail.com")
print (Njiiri_contact.name)
print (Ndungu_contact.email)
