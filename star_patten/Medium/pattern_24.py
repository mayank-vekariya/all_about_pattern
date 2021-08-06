def Pattern_Programs(n):
	osp=n-1
	for i in range(1,n+1):
		if i==1 or i==n:
			print(" "*osp+"*"*n)
		else:
			print(" "*osp+"*"+" "*(n-2)+"*")
		osp-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))