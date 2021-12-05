a = "Hello World"
print(a)

#multiline string..
b = """Python is a programming language
	It is an oop.
	I enjoy to code in python."""
print(b)

B = "Hello World!"
print(B[1])

#slicing...
print(B[2:5])
print(B[-1])
print(B[-6])
print(B[-5:-2])

#check string length..
print(len(a))
print(len(B))
print(len(b))

#stip() method
z = " python "
print(z)
print(z.strip())

#upper case..
print(z.upper())

print(z.lower())

#replace() method..
print(B.replace("H","K"))

print(b.replace("Python","php"))

#split string..
print(B.split(","))

#ckeck character present or not..
txt = "The rain in spain stays mainly in plain"
x = "ain" in txt 
print(x)
x = "ain" not in txt
print(x)

#string concatenation..
w = "Shreya"
v = "Rani"
print(w+v)
y = w+ " "+v
print(y)

#string format..
age=36
txt="My name is John,and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "\nI want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#by using index number..
quantity = 3
itemno = 567
price = 49.95
myorder = "\nI want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#Boolean values....
print(10>9)
print(10==9)
print(10<9)

x = 200
print(isinstance(x,int))
