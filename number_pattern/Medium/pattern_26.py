def Pattern_Programs(n):
	hh=n
	for i in range(1,n+1):
		for j in range(hh,n+1):
			print(j,end="")
		for k in range(hh-1):
			print(n,end="")
		print()
		hh-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))