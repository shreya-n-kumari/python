l = [5,1,8,9,6]
search = 6
result = -1
for i in range(len(l)):
	if search == l[i]:
		result = i
		break
print(result)