def Pattern_Programs(n):
	sp=0
	for i in range(n*2-1,0,-2):
		print(" "*sp+"*"*i)
		sp+=1

if __name__ == '__main__':
	Pattern_Programs(int(input()))