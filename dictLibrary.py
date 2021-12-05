import collections
defaults = {
		"appetizers": "Humans",
		"main": "Pizza",
		"desert": "Chocolate Cake",
		"dink": "Water",
}

def prep_menu(customizations):
	return
collections.ChainMap(customizations,defaults)
def print_menu(menu):
	for key,value in menu.items():
		print("As {key} : {value}.")
if __name__ == '__main__':
	menu1 = prep_menu({})
	print_menu(menu1)