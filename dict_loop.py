glossary = {"loop":'iteratation','if':'check condition','break':'To exit','function':'small program','list':'array'}
print(glossary['loop'])
for key,value in glossary.items():
	print(key + " : " + value) #looping through key value.


print("\n....next program....")
river ={'ganga':'india','nile':'egypt','punpun':'indiaa'}
for key,value in river.items():						#looping through key,value.
	print("The "+ key +' runs throuh ' +value)

print("\nlooping through key....")
for key in river:
	print(key.title())

print("\n..looping through value..")
for value in river.values():
	print(value.title())

print("\n loop through the list of people who should take the poll.")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',	
	'edward':'c',
	'shre': 'python',
	}

for name in favorite_languages.keys():
	print(name.title() + ",Thank you for taking the poll.")

if 'shreya' not in favorite_languages:
	print("Shreya,please take our poll.")