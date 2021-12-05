employes = [['shreya',22,'developer'],['dekosta',25,'security'],['alina',30,'sales']]
print(employes)							#print the all list.
for employe in employes:
	print(employe)						#print the sub lists.
for employee in employes:
	print('Name:',(employee[0]))
	print('Age: ',  employee[1])
	print('Department:',employee[2])
	print('-' * 20)

employee = employes[1]					#print the list which is at index 1.
print(employee)
print('Name:',employee[0])
print('Age: ', employee[1])
print('Department:', employee[2])
print('.'*25)