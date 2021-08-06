def Pattern_Programs(n):
	osp=n-1
	for i in range(1,n+1):
		print(" "*osp,end="")
		for j in range(1,i+1):
			print(j,end=" ")
		print()
		osp-=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))