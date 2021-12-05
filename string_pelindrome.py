mystr = "Madam"
#convert entire string to either lower or upper.
mystr = mystr.lower()

#reverse string.
revstr = reversed(mystr)

#check if the string is equal to its reverse
if list(mystr) == list(revstr):
	print("Given string is pelindrome")
else:
	print("Given string is not pelindrome")