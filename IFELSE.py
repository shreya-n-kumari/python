a = 22
b = 200
if b>a:
	print("b is greater then a")

a = 22
b = 22
if b>a:
	print("b is greater than a")
elif a==b:
	print("\na is equal to b")

a = 22
b = 200
if a>b:
	print("b is greater than a")
elif a==b:
	print("a is equal to b")
else:
    print("b is greater than a")

#short hand if
if b>a : print("\nb is greater than a")

#short hand if else..
print("\nA") if b>a else print("\nB")
print("\nA") if a>b else print("\nB")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 220
b = 55
c = 330
if a>b and c>a:
	print("both condition true")
a = 220
b = 55
c = 330	
if a>b or b>c:
	print("atleast one is true")

if a>b :
	pass
