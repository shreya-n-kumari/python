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
