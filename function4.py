def city_country(city,country):
	full_name = city+ ', ' +country
	return full_name.title()

your_choice = city_country("banglore","india")
print(your_choice)
your_choice = city_country("paris","france")
print(your_choice)
your_choice = city_country("shantiago","chille")
print(your_choice)



def make_album(artist,song, trcks=' '):
	"""Return a dictionary of information about a album."""
	album = {'singer': artist , 'song': song}		#dictionary...
	if trcks:
		album['trcks'] = trcks
	return album

musician = make_album('jubin','khalibali',trcks=5)
print("\n",musician)


#>>>>>>>>>>>>PASSING THE LIST>>>>>>>>>>>>>>>>>
def greet_user(names):
	"""print a simple greeting to each user in the list"""
	for name in names:
		msg = "Hello, " +name.title()+ "!"
		print(msg)

usernmae = ['shreya','savi','avi','gungun']
greet_user(usernmae)


