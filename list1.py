print("Enter the number of elements in list")
N = int(input())
l = []
res= []
for i in range(N):
	l.append(i)
print(l)


print("Enter integer to be inserted in list:")
e = int(input())
print("Enter index number where you want to insert integer")
p = int(input())

l.insert(p,e)
print(l)



