def make_album(artist,album,no_tracks = 0):
	"""Return a dictionary of information about a album."""
	songs = {"name" : artist,"album" : album}
	if no_tracks:
		songs['tracks'] = no_tracks
	return songs

music = make_album("arijit sigh","ms dhoni",20)	#20 is optional args.
print(music)
music = make_album("Jubin Nautiyal","Marjaavan")
print(music)
N = make_album("Neha Kakkar","party songs")
print(N)