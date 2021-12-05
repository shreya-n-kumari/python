a = eval(input())
b = eval(input())

i =1
#for i in range(1,a*b+1):
while True:

	if i%a == 0 and i%b == 0:
		print("Least Common Multiple : ",i)
	break
	i += 1