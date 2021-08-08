def Pattern_Programs(n):
	for i in range(1,n+1):
		temp=1
		for j in range(i):
			print(temp,end=" ")
			if temp==1:
				temp=0
			else:
				temp=1
		print()


if __name__ == '__main__':
	Pattern_Programs(int(input()))