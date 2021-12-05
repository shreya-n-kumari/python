print('Enter Your Name : ')
name = input()
filename = 'guest.txt'
with open (filename,'w') as object:
	(object.write(name))
	


