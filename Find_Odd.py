#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

max = int(input("Enter max number : "))
odd_li = []

for i in range(1,max):
	if i % 2 == 1:
		odd_li.append(i)

print(odd_li)
