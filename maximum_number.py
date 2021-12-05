l = [4,5,11,3]
maximum = 0

for number in l:
	if number > maximum:
		maximum = number

print(maximum)
print(max(l))

z = []
for number in range(1,101):
	z.append(number) 
	#print(number)
print(z)
print(max(z))
print(min(z))
print(sum(z))