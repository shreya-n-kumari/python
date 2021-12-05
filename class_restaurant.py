#Excerise 9.1
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

#Excerise 9.4.....
	 def set_number_served(self):
			print("The number of people served here is " + str(self.number_served))

	 def increment_number_served(self,num):
	 	self.number_served += num

#excerise 9.6..........................

class IceCreamStand(restaurant):
	 def __init__(self,restaurant_name,cuisine_type,flavor):
	 	super().__init__(restaurant_name,cuisine_type)
	 	self.flavor = flavor

	 def DispalyFLavor(self):
	 	print("Flavours are : ",self.flavor)



if __name__ == '__main__':
	res=restaurant('the baloon',6)
	res.describe_restaurant()
	res.open_restaurant()
	res.increment_number_served(10)
	res.set_number_served()

	print("\n")
	my_rest = restaurant('barbeque',8)
	my_rest.describe_restaurant()
	my_rest.open_restaurant()
	my_rest.increment_number_served(20)
	my_rest.set_number_served()

	print("\n")
	rest = restaurant('chhapan',12)
	rest.describe_restaurant()
	rest.open_restaurant()

	res.set_number_served()
	res.increment_number_served(101)
	res.set_number_served()

	Ice = IceCreamStand('Ice parlour',5,'vanilla')
	Ice.describe_restaurant()
	Ice.DispalyFLavor()