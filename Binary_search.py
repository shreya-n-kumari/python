l = [2,3,5,8,11,12,18]
print("Enter search Element")
search = int(input())
lower = 0
upper = len(l)-1
found = False
while lower <= upper and not found:			
	mid = (lower + upper)// 2				
	if l[mid] == search:
		found = True
	elif search < l[mid]:
		upper = mid-1
	else:
		lower = mid+1

if found == False:
	print('value not found')
else:
	print('value found at index ',mid)

