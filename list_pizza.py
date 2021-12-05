def make_pizza(size,*toppings):
	"""sumarise pizza we are about to make"""
	print("\nMaking a "+str(size)+ "-inch pizza with the following toppings:")
	for topping in toppings:
		print("-",topping)


pizza = ['babycorn','macroni','paneer']
friend_pizza = pizza[:]
print(pizza)
print(friend_pizza)

pizza.append("chilly")
friend_pizza.append("magrita")

print(pizza)
print(friend_pizza)

print("My Favorite pizza are:")
for fav in pizza:
	print(fav)

print("\n")
print("My friend's favorite pizza are:")
for fav in friend_pizza:
	print(fav)