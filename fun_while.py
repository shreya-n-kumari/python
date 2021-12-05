songs = {}
def make_album(artist,album,no_tracks = 0):
	"""Return a dictionary of information about a album."""
	
	i = 0
	while i < 2:
		print("Enter 'q' to exit")

		title = input("Enter song name ")
		if title == 'q':
			break
		artist = input("Enter singer name ")
		if artist == 'q':
			break
		songs[title] = artist
		i+=1

make_album('artist','title')
print(len(songs))
print(songs)
for artist,album in songs.items():
	print(artist, ":", album)