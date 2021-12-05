with open('python.txt') as file_object:
	contents = file_object.read()
	print(contents.replace('python','java'))	#use the replace() method to replace any word in astring with a different word.
	#print(contents)

#Reading line by line.
filename = 'python.txt'
with open(filename) as object:
	for line in object:
		print(line.rstrip())


#Making a list of lines from a file
filename = 'python.txt'
with open (filename) as object:
	lines = object.readlines()
	"""counting total letters"""
	string = ' '
	for line in lines:
		string += line.strip()
		print(line.rstrip())
		print(len(line))
	