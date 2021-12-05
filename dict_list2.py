#example of list in a dictionary.
favorite_number = {
				'shreya': [25,20,'first'],
			    'rubina': [30,23,'fifth'],
				'nikita': ['sixth',40,45],
			}

for name,value in favorite_number.items():
	print(name.title(), "'s favorite number are :")
	for num in value:   	#looping through list(value) in dictionary.
		print('\t',num)