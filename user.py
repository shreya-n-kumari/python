class User:

	def __init__(self):
		self.id=0
		self.name=""
		self.address=""

	def set_id(self, id):
		self.id = id
	
	def set_name(self, name):
		self.name = name

	def set_address(self, address):
		self.address = address	

	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_address(self):
		return self.address

########### User class ends ############


def displayUserDetails(user):
	print("---> Id:: ", user.get_id())
	print("---> name:: ", user.get_name())
	print("---> address:: ", user.get_address())

def displayUserDetails2(user):
	print("\n---> Id:: ", user2.get_id())
	print("---> name:: ", user2.get_name())
	print("---> address:: ", user2.get_address())

if __name__ == '__main__':
	user = User()			#defining class User in a variable called user.
	user.set_id(1)
	user.set_name("abc")
	user.set_address("patna")

	user2 = User()
	user2.set_id(2)
	user2.set_name("Elon Musk")
	user2.set_address("India")

	displayUserDetails(user)
	displayUserDetails2(user)

		