print("Enter Your Name : ")
print("Enter q to exit : ")

filename = 'guest_book.txt'

with open (filename,'a') as object:

	while True:

		name = input()
		print("Hello",name,"\n")
		if name == 'q':
			break
		name=name+"\n"
		object.write(name)
	