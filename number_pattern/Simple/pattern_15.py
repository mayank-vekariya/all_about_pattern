def Pattern_Programs(n):
	hh=n+1
	osp=0
	for i in range(1,n+1):
		print(" "*osp,end="")
		for j in range(1,hh):
			print(j,end=" ")
		print()
		hh-=1
		osp+=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))