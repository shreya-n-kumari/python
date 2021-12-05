x = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
y = [[13,14,15,26],[16,17,18,25],[19,20,21,22]]
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
print('addition of atrix')

for i in range(len(x)):
	for j in range(len(x[0])):
		result[i][j] = x[i][j] + y[i][j]

print(result)

print('subtraction of matrix')
for i in range(len(x)):
	for j in range(len(x[0])):
		result[i][j] = x[i][j] - y[i][j]

print(result)

for r in result:
	print(r)