def Pattern_Programs(n):
	temp=1
	for i in range(1,n*2):
		print(str(i)*temp)
		if i<n:
			temp+=1
		else:
			temp-=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))