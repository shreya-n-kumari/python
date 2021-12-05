import math

def Is_prime(x):
	for i in range(2,x):
		#print(i)
		if (x % i) == 0:	
			return False
	return True

if __name__ == '__main__':
	print(Is_prime(7))
	print(Is_prime(100))
	print(Is_prime(53))