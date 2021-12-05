stored = {0:0 , 1:1}	#set the 2 term of the fibonacci series.
def fibonacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibonacci(n-2) + fibonacci(n-1)

def fibonacci_dynamic(n):
	if n in stored:
		return stored[n]
	else:
		stored[n] = fibonacci_dynamic(n-2) + fibonacci_dynamic(n-1)

if __name__ == '__main__':
	print(fibonacci_dynamic(10))		#ERRORRRRRRRRRRRRRRRRRRRRRRRRRR
	print(fibonacci(10))