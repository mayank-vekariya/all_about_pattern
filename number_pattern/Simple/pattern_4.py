def Pattern_Programs(n):
	hh=n
	for i in range(1,n*2):
		for j in range(1,hh+1):
			print(j,end="")
		print()
		if i<n:
			hh-=1
		else:
			hh+=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))