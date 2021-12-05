x = [[1,2],[3,4],[5,6]]
y = [[1,2,3,4],[5,6,7,8]]
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(x)):
	for j in range(len(y[0])):

		for k in range(len(y)): #iterating by rows of y.
			result[i][j] += x[i][k] * y[k][j]

print(result)

for r in result:
	print(r)