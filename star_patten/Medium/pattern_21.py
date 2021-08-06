def Pattern_Programs(n):
	osp=n-1
	insp=-1
	for i in range(1,n*2):
		if i==1 or i==n*2-1:
			print(" "*osp+"*")
		else:
			print(" "*osp+"*"+" "*insp+"*")
		if i<n:
			osp-=1
			insp+=2
		else:
			osp+=1
			insp-=2



if __name__ == '__main__':
	Pattern_Programs(int(input()))