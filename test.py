import math
x = 14
x += 1
print(x/5)
print ((x/5)**2)

#find first number greater than 100 and divisible by 17.
i = 100
while i<= 1000:
	i += 1
	if i % 17 == 0:
		print(i, "is the first number greater than 100 which is divisible by 17")
		break

#finding LCM..
first_divisor = 24
second_divisor = 36

counting = True
i = 1
while counting:
	if i % first_divisor == 0 and i % second_divisor == 0:
		print('The Least Common Multiple of',first_divisor, 'and',second_divisor,'is',i,'.')
		break
	i += 1
	

