def make_shirt(size,text):
	"""making shirt with text you given"""			
	print("\n",size)
	print(text.title())


if __name__ == '__main__':
	make_shirt(30,"i love python")		#calling with positional argument.
	make_shirt(32,text = 'i love python')		#calling by keyword argument.


#.............OPTIONAL ARGUMENT.................
def get_formatted_name(first_name, last_name, middle_name=''):
	 """Return a full name, neatly formatted."""
	 if middle_name:
			full_name = first_name + ' ' + middle_name + ' ' + last_name
	 else:
			full_name = first_name + ' ' + last_name
	 return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


