def Pattern_Programs(n):
	for i in range(1,n*2):
		if i==n:
			print("*"*(n*2-1))
		else:
			print(" "*(n-1)+"*")


if __name__ == '__main__':
	Pattern_Programs(int(input()))