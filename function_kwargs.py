#keyword argument.....
def car_info(model_name,manufacturer,**more_info):
	make_car = {}
	make_car['name'] = model_name
	make_car['company'] = manufacturer
	for key,value in more_info.items():
		make_car[key] = value
	return make_car

car = car_info('toyota','maruti',color = 'blue',tow_package = True)
print(car)