def Pattern_Programs(n):
	temp=1
	for i in range(1,n*2):
		for j in range(1,temp+1):
			print(j,end="")
		for k in range(temp-1,0,-1):
			print(k,end="")
		print()
		if i<n:
			temp+=1
		else:
			temp-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))