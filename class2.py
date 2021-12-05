"""Importing singal class"""
from class_car import car

my_car = car('audi','a4',2016)
print(my_car.get_name())

my_car.odometer_reading = 45
my_car.read_odometer()