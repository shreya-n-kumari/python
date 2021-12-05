#>>>>>>>>FUNCTION WITH A WHILE LOOP>>>>>>>>>>>
def get_name(first_name,last_name):
	"""Return a full name neatly formatted"""
	full_name = first_name + ' '+ last_name
	return full_name.title()


#This is an infinite loop!
while True:
	print("\nplease enter your name")
	print("(enter 'q' at any time to quit")
	f_name = input("first name : ")
	if f_name == 'q':
		break

	l_name = input(" last name : ")
	if l_name == 'q':
		break

	formatted_name = get_name(f_name,l_name)
	print("\nHello " +formatted_name+ "!")
