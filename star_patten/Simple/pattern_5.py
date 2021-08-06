def Pattern_Programs(n):
	sp=n-1
	for i in range(1,n*2+1,2):
		print(" "*sp+"*"*i)
		sp-=1

if __name__ == '__main__':
	Pattern_Programs(int(input()))