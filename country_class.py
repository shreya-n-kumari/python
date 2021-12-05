class Country():
    def __init__(self, name='Unspecified', population=None, size_kmsq=None):	#keyword argument.
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    def __str__(self):
    	return self.name
if __name__ == '__main__':
	usa = Country(name='United States of America', size_kmsq=9.8e6)
	print(usa.__dict__)			#Dictionary output of usa object.

	chad = Country(name = 'chad')
	print(chad)

	chad = Country(name = 'algeria')
	print(chad)