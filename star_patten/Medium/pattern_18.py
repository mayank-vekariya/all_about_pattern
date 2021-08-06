def Pattern_Programs(n):
	osp=0
	insp=n-3
	for i in range(1,n+1):
		if i == n:
			print(" "*osp+"*")
		elif i == 1:
			print("*" * n)
		else:
			print(" "*osp+"*" + " " * insp + "*")
			insp -= 1
		osp+=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))