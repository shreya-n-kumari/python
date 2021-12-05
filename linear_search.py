def search(arr,l,data):
	for i in range(0,l):
		if (arr[i] == data):
			return i
		else:
			return -1

if __name__ == '__main__':
	
	arr = [2,9,8,55,10,11,25,30]
	l = len(arr)
	data = input("enter data to be search : ")

	result = search(arr,l,data)
	

	if (result == -1):
		print('value of result',result)
		print('Element is not found in the list.')
	else:
		print('data found at index : ',result)
		

			