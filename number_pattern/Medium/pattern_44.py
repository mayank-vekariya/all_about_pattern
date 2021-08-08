def Pattern_Programs(n):
	temp=1
	for i in range(1,n*2):
		count=temp
		for j in range(temp):
			print(count,end=" ")
			count+=1

		for k in range(count-2,temp-1,-1):
			print(k,end=" ")
		print()
		if i<n:
			temp+=1
		else:
			temp-=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))