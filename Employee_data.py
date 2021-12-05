employe = [{'Name': 'Shreya', 'Age': '20', 'department': 'devloper'},{'Name': 'Lisa','Age':'25','department':'security'},{'Name':'Haden','Age':'30','department': 'sales'}]
print(employe)      #define dictionary within list.

for employee in employe:
	print('Name:', employee['Name'])
	print('Age:' ,employee['Age'])
	print('department:', employee['department'])
	print('-' * 20)

for employ in employe:
	if employ['Name'] == 'Shreya':
		print('Name:', employ['Name'])
		print('Age:' ,employ['Age'])
		print('department:', employ['department'])