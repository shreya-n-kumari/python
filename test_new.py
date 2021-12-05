def example():
	pass


"""def noLimit(**names):
	print(names["fname"])
	print(names["lname"])

if __name__ == '__main__':
	example()
	#print(add(2))
	noLimit(fname='abc', lname='def')"""

def factorial(n):
	if n > 0:
		return n*factorial(n-1)

print(factorial(5))