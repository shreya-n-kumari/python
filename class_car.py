"""A Class that represent a Car. """
class Car():
	def __init__(self,model,make,year):
		"""Initialisng attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_name(self):
		long_name = str(self.year)+ " " +self.make + ' '+self.model
		return long_name.title()

	def read_odometer(self):
		"""print a statement showing the car's mileage"""
		print("this car has " +str(self.odometer_reading) + " miles on it.")

	def update_odometer(self,mileage):
		"""set the odometer reading to the given value."""
		self.odometer_reading = mileage

	def increment_odometer(self,miles):
		self.odometer_reading += miles

class ElectricCar(Car):
	"""Models aspects of a car, specific to electric vehicles."""
	def __init__(self,make,model,year):
		"""Initialize attribute of the parent class
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(make,model,year)
		self.battery_size = 80					#defining attribute and method

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

