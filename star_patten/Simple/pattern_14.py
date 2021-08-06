def Pattern_Programs(n):
	star=n
	osp=0
	for i in range(1,n*2):
		print(" "*osp+"* "*star)
		if i<n:
			star-=1
			osp+=1
		else:
			star+=1
			osp-=1

if __name__ == '__main__':
	Pattern_Programs(int(input()))