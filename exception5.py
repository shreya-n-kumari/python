filename = 'python.txt'
try:
	with open(filename) as object:
		print(filename)
except Exception:
	print("please try again after sometime. we're working on it.")
