#exercise 8-11
def show_magician(names):
	for name in names:
		print("Hello "+name.title()+ "!")

def make_great(names):	#modify list
	l = []
	for name in names:
		l.append("The Great "+ name.title())
	return l


magic = ['tom','jerry','oogy']
result = make_great(magic)

show_magician(magic)
show_magician(result)	