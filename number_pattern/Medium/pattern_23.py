def Pattern_Programs(n):
	for i in range(1,n+1):
		for j in range(n,i,-1):
			print(j,end="")
		for k in range(i):
			print(i,end="")
		print()


if __name__ == '__main__':
	Pattern_Programs(int(input()))