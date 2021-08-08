def Pattern_Programs(n):
	hh=1
	osp=0
	for i in range(1,n*2):
		print(" "*osp,end="")
		for j in range(hh,n+1):
			print(j,end="")
		print()
		if i<n:
			hh+=1
			osp+=1
		else:
			hh-=1
			osp-=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))