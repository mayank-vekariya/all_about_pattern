def Pattern_Programs(n):
	osp=n-1
	insp=1
	for i in range(1,n+1):
		if i==1:
			print(" "*osp+"*")
		elif i==n:
			print("*"*(n*2-1))
		else:
			print(" "*osp+"*"+" "*insp+"*")
			insp+=2
		osp-=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))