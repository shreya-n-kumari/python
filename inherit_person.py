class person():
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name

	class baby(person):
			def speak(self):
				print("Hello Everyone!")

	class adult(person):
			def speak(self):
				print('hello my name is %s' %self.first_name)


if __name__ == '__main__':
	sara = baby('sara','khan')
	tar = adult('tara','sutariya')
	print(sara.speak())
	print(tar.speak())