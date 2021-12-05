#excrise 9.3......
class user():
	def __init__(self,first_name,last_name,locatio,gender):
		"""Initialize attribute of the parent class"""
		self.f_name = first_name
		self.l_name = last_name
		self.location = locatio
		self.gender = gender
		self.login_attempts = 0

	def describe_user(self):

		print(self.f_name.title() , end = ' ')
		print(self.l_name.title())
		print(self.location.title())
		print(self.gender.title())
		

	def greet_user(self):
		print('Hello',self.f_name.title() + ' '+self.l_name.title()+'!')

#Excerise 9.5..............
	def increment_login_attempt(self):
		self.login_attempts += 1

	def displayLogin(self):
		print("Login Attempts after Incremnt",self.login_attempts)

	def Reset_attempt(self):
		self.login_attempts = 0
	
class Admin(user):
	def __init__(self,first_name,last_name,locatio,gender,previlege):
		super().__init__(first_name,last_name,locatio,gender)
	

if __name__ == '__main__':
	person = user('shreya','rani','naubatpur','female')
	person.describe_user()
	person.greet_user()
	person.increment_login_attempt()
	person.displayLogin()
	person.increment_login_attempt()
	person.displayLogin()
	person.Reset_attempt()
	person.displayLogin()