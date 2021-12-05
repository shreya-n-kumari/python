class restaurant:
	 def __init__(self,restaurant_name,cuisine_type):
	 	"""initialize restaurant name and cusine"""
	 	self.restaurant_name = restaurant_name
	 	self.cuisine_type = cuisine_type
	 	self.number_served = 0 			#setting default value for an attribute
		

	 def describe_restaurant(self):
	 	print(self.restaurant_name.title())
	 	print('cusine = ',self. cuisine_type)

	 def open_restaurant(self):
	 	print(self.restaurant_name.title() + " is open now. Thank You!")



class IceCreamStand(restaurant):
	 def __init__(self,restaurant_name,cuisine_type,flavor):
	 	super().__init__(restaurant_name,cuisine_type)
	 	self.flavor = flavor

	 def DispalyFLavor(self):
	 	for i in flavor:
	 		print("Flavours are : ",self.flavor)

list = []

if __name__ == '__main__':
	res = restaurant('the arch',8)
	res.describe_restaurant()
	res.open_restaurant()

	icecream = IceCreamStand('the velvat',5)
	list.append = IceCreamStand('vanilla')
	list.append = IceCreamStand('chocolate')
	list.append = IceCreamStand('strawberry')
	icecream.DispalyFLavor()

