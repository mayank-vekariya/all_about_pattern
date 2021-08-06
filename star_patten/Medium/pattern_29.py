def Pattern_Programs(n):
	osp=1
	insp=2*n-5
	for i in range(1,n*2):
		if i==1 or i==n*2-1:
			print("* "*n)
		else:
			if i==n:
				print(" "*osp+"*")
			else:
				print(" "*osp+"*"+" "*insp+"*")
			if i<n:
				insp-=2
				osp+=1
			else:
				insp+=2
				osp-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))