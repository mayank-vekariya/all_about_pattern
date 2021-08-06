def Pattern_Programs(n):
	insp=0
	osp=n-2
	for i in range(1,n*2):
		if i==n*2-1 or i==1:
			print(" "*(n-1)+"*")
		else:
			print(" "*osp+"*"+" "*insp+"*")
			if i<n:
				insp+=1
				osp-=1
			else:
				insp-=1
				osp+=1
if __name__ == '__main__':
	Pattern_Programs(int(input()))