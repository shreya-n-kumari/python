filename = 'dogs.txt'
try:
	with open(filename)as f_obj:
		contents = f_obj.read()
		print(contents)
except FileNotFoundError:
	pass		#failing silently.