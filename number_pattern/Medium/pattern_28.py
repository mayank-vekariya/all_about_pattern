def Pattern_Programs(n):
	star=1
	for i in range(1,n*2):
		temp=i
		for j in range(star):
			print(temp,end=" ")
			temp+=i
		print()
		if i<n:
			star+=1
		else:
			star-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))