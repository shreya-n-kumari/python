#sorting numbers using bubble sort in a list.

l = [5,8,1,3,6]
print("before sorting:-" , l)
swapping = True
while swapping:
	swapping = False
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			l[i],l[i+1] = l[i+1],l[i]
			swapping = True
print("after sorting:-", l)