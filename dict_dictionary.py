#Example of A dictionary in dictionary.
cities = {
		'patna':{
			'country':'india',
			'population':'1cr',
			'fact':'no mnc in this city'
			},
		'chennai':{
			'country':'usa',
			'population':'1.5cr',
			'fact':'sea in this city.'
			},
		'bengaluru':{
			'country':'india',
			'population':'2cr',
			'fact':'IT city of india',
			},
	}
for city,city_info in cities.items():
	print("city:"+ city)				#printing main dictionary key.
	info = city_info['country']+ " " +city_info['population'] + " " +city_info['fact']
	print(info)							#printing main dictionary value.
	print("\n values with key")
	for k,v in city_info.items():
		print(k + ':'+v)