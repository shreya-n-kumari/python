def build_profile(first,last,**your_info):
	"""build a dictionary containing everything we know about you"""
	profile = {}
	profile['first_nmae'] = first
	profile['last_name'] = last
	for key, value in your_info.items():
		profile[key] = value
	return profile

your_profile = build_profile('shreya','rani',location = 'patna',field = 'computer science',
								degree = 'mca')
print(your_profile)



"""from pizza import make_pizza
make_pizza(16,'peproni')
make_pizza(25,'mashrom','green pepper','pastapizza','baby corn','extra cheese')"""

