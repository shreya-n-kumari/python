l = [eval(x) for x in input("enter element").split(",")]
print(l)
element = eval(input("enter element value "))
i = 0
while i<len(l):
	if l[i] == element:
		print(i,end = ' ')
	i+=1