def Pattern_Programs(n):
	osp=0
	insp=n
	for i in range(1,n+1):
		if i==n:
			print(" "*osp+"*")
		elif i==1:
			print("*"*(n*2-1))
		else:
			print(" "*osp+"*"+" "*insp+"*")
			insp-=2
		osp+=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))