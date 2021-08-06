def Pattern_Programs(n):
	hh=n
	for i in range(1,n+1):
		for j in range(n,hh-1,-1):
			print(j,end="")
		print()
		hh-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))