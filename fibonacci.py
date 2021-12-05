import math

def fibonacci(n):
    previous = 0
    current = 1
    for i in range(n-1):
    	new = current
    	current = previous + current
    	previous = new
    return current
	
if __name__ == '__main__':
 	print(fibonacci(6))