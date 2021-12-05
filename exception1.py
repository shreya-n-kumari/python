print("Enter Two Numbers, And I'll sum It")
print("enter q to quit")
first_num = 0
sec_num = 0
while True:
	try:
		first_num = input("\nFirst number - ")
		
		sec_num = input("\nSecond number - ")

		answer = int(first_num) + int(sec_num)
		print("sum is = ",answer)
	
	except ValueError:
		print("you have entered wrong value!!")
		print(first_num)
		if first_num == 'q':
			print("inside q condition")
			break
print("closing program")


		