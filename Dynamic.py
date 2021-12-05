stored_result = {}
def sum_to_n(n):
	result = 0
	for i in reversed(range(n)):
		if i+1 in stored_result:
			print('Stopping sum at %s because we have previously computed it' % str(i + 1))
			result += stored_result[i+1]
			break
		else:
			result += i + 1
    stored_results[n] = result				#ERRORRRRRRRRRRRRRRRRRRRRRRRRR
    return result

if __name__ == '__main__':
	print(sum_to_n(5))