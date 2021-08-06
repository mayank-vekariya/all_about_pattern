def Pattern_Programs(n):
	hh=n+1
	for i in range(1,n+1):
		for j in range(1,hh):
			print(j,end="")
		print()
		hh-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))