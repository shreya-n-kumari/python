class Student:
	num=100

	def __init__(self):
		print("empty constrcutor of student class")
		self.addr="hell student"
	
	def __init__(self, rollNo, name):
		print("paramterized constrcutor call")
		self.rollNo = rollNo
		self.name = name
		self.num=1000

	def displayStudentName(self):
		print(self.rollNo)
		print(self.name)
		print(self.num)



if __name__ == '__main__':
	#student1 = Student()
	#student1.displayStudentName()

	student2 = Student(5, "xyz")
	student2.displayStudentName()