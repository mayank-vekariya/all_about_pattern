def Pattern_Programs(n):
	star=n
	for i in range(1,n*2):
		print("*"*star)
		if i<n:
			star-=1
		else:
			star+=1

if __name__ == '__main__':
	Pattern_Programs(int(input()))