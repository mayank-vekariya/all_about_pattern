def Pattern_Programs(n):
	hh=1
	for i in range(1,n+1):
		for j in range(1,hh+1):
			print(j,end="")

		for k in range(hh-1,0,-1):
			print(k,end="")
		print()
		hh+=1
if __name__ == '__main__':
	Pattern_Programs(int(input()))