def Pattern_Programs(n):
	osp=n-1
	hh=1
	for i in range(1,n*2):
		print(" "*osp,end="")
		for j in range(1,hh+1):
			print(j,end=" ")
		print()
		if i<n:
			osp-=1
			hh+=1
		else:
			osp+=1
			hh-=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))