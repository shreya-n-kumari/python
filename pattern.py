def star(N):
	for i in range(0,N):
		for j in range(0,i+1):
			print("*",end = "")
		print("\r")

if __name__ == '__main__':
	N = int(input())
	star(N)
