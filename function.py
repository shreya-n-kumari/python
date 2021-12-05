#Defining and Calling the Function in Shell.
def add_up(x,y):
	return x+y

if __name__ == '__main__':
	print(add_up(1,3))
	#print(sum)



def getSecondElement(mylist):	#defining function.
	if len(mylist) > 1:
		return mylist[1]
	else:
		'List was too small!'

if __name__ == '__main__':
	lst = getSecondElement([1,2,3,4])		#calling the function.
	print(lst)