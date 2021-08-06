def Pattern_Programs(n):
	for i in range(1,n*2):
		if i==1 or i==n or i==n*2-1:
			print("*"*(n-2))
		else:
			print("*"+" "*(n-4)+"*")


if __name__ == '__main__':
	Pattern_Programs(int(input()))