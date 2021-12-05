print("Enter Two Numbers, And I'll sum It")
try:
	first_num = int(input("\nFirst number - "))
		
	sec_num = int(input("\nSecond number - "))

except ValueError:
	print("you have entered wrong value!!")

else:
	answer = first_num + sec_num
	print(answer)