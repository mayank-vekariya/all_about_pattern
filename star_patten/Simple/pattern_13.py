def Pattern_Programs(n):
	sp=0
	star=n
	for i in range(1,n*2):
		print(" "*sp+"*"*star)
		if i<n:
			sp+=1
			star-=1
		else:
			sp-=1
			star+=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))