import math

def sum_first_n(n):
    result = 0
    for i in range(n):
        result += i + 1
    return result

if __name__ == '__main__':
	print(sum_first_n(100))
