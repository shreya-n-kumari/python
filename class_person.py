class person():
	def __init__(self,first_name,last_name):
		self.f_nmae = first_name
		self.l_name = last_name

	@property 
	def full_name(self):
		return '%s %s' %(self.f_nmae , self.l_name)


if __name__ == '__main__':
	per = person('marry','com')
	print(per.full_name())