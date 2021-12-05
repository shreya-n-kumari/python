animals = ['dog','rabbit','elephant']
for animal in animals:
	print(animal)
	print(animal.title())
	print(animal.title() +",would make a great pet\n")
print("Any of these make a greate pet!")

#range() function in pyhton.
for value in range(1,5):
	print(value)

numbers = list(range(1,5))
print(numbers)

print("\nsquare of first 10 natual numbers")

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

print("\nodd numbers--")
odd_numbers= list(range(1,21,2))
print(odd_numbers)

print("\ncubes of first 10 natural numbers USING LIST COMPREHENSION")
cubes = [value**3 for value in range(1,11)]
print(cubes)

print("\nprint numbers from 1 to 20")
for numbers in range(1,21):
	print(numbers)
	
#print(max(numbers))


#Tuple example..
dimensions = (200,50)
print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

