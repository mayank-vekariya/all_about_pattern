def Pattern_Programs(n):
	hh=1
	for i in range(1,n+1):
		for j in range(i):
			print(hh,end="")
			hh+=1
		print()


if __name__ == '__main__':
	Pattern_Programs(int(input()))