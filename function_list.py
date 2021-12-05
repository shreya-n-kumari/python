def show_magician(names):
	for name in names:
		print("Hello "+name.title()+ "!")

def make_great(names):	#modify list
	i = 0
	for name in names:
		names[i]="The great "+ name
		i+=1




magic = ['tom','jerry','oogy']
show_magician(magic)	#passing list in function
make_great(magic)
show_magician(magic)