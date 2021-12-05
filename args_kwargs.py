#from coustmer import formate_coustmer

def formate_coustmer(first, last ,location):
	full_name = '%s' '%s' %(first,last)
	if location:
		return '%s (%s)' %(full_name,location)
	else:
		return full_name



if __name__ == '__main__':

	print(formate_coustmer('Lilly ', 'jokowich',location = 'california'))

	#print(formate_coustmer('shree','chahal'))