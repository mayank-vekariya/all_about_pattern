def Pattern_Programs(n):
	osp=0
	insp=n-2

	for i in range(0,n):
		if i==n//2:
			print(" "*osp+"*")
		else:
			print(" "*osp+"*"+" "*insp+"*")
		if i<n//2:
			osp+=1
			insp-=2
		else:
			osp-=1
			insp+=2

if __name__ == '__main__':
	Pattern_Programs(int(input()))