class user:
	def __init__(self):
		self.name = ''
		self.age = 0
		self.address = ''


def set_name(self,name):
	self.name = name
	
def set_age(self,age):
	self.age = age

def set_address(self,address):
	self.address = address
	

def get_name(self):
	return self.name

def get_age(self):
	return self.age

def get_address(self):
	return self.address



class coustomer(user):

	def __init__(self):
		super().__init__()
		self.service = ''
		self.gender = ''


def set_sevice(self,service):
	self.service = service

def set_gender(self,gender):
	self.gender = gender


def get_service(self):
	return self.service

def get_gender(self):
	return self.gender



class student(user):
	def __init__(self):
		super().__init__()
		self.rollno = 0
		self.class_name  = ''


def set_roll(self,rollno):
	self.rollno = rollno

def set_class(self,class_name):
	self.class_name = class_name


def get_roll(self):
	return self.rollno

def get_class(self):
	return self.class_name


if __name__ == '__main__':
	coustomer = coustomer()
	coustomer.set_sevice("facial")
	coustomer.set_gender('Femail')
	coustomer.set_name('disha')
	coustomer.set_age(25)
	print(coustomer)









