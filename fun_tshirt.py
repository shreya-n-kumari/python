def make_shirt(size,message):
	print("size : ",size)
	print("message : ",message)
	"""OR"""
	print("The Size of the shirt is "+str(size)+" and message is "+message)

make_shirt(32,'social distance')	#positional argument
make_shirt(message = 'I hate liers',size = 32)	#keyword argume.

def update_shirt(size = 'L',message = 'I Love Python'):
	print("\nThe size of shirt is "+size+" message on it : "+message)

update_shirt()	#calling default function.
update_shirt(size = "M")