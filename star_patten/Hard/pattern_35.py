def Pattern_Programs(n):
	for i in range(1,n+1):
		if i%2==0:
			print(" "+"* "*(n-3))
		else:
			print("* "*(n-2))


if __name__ == '__main__':
	Pattern_Programs(int(input()))