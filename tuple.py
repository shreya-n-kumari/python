t = ('bread','milk','eggs')
print(len(t))  

""" As tuples are immutable ,items cannot be append
or cannot be change."""

print(t + ('orange','mango'))  

"""we can create a new tuple by concatenating the existing tuple with other new items.
As in the above code"""

print(t)

t_mixed = 'apple',True,3
#tuples are also support mixed type and nesting.

print(t_mixed)

shopping = ('apple', 3),('gauava',6),('lichi',12)

#we can also declare a tuple without using parantheses. As shown in above code.
print(shopping)

print("\n")
buffet = ('pasta','maggie','paneer_chilly','babycorn')
print(buffet)
for food in buffet:
	print(food)
	
print("\n")

"""Tuple can't be modified. so for replacing some items with different food 
we have to redefine the entire tuple"""
buffet = ('pasta','maggie','pizza','manchurian')
for food in buffet:
	print(food)