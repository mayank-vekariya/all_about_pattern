def Pattern_Programs(n):
	hh=1
	for i in range(1,n+1):
		kk=hh
		for j in range(i):
			print(kk,end=" ")
			kk+=n
		print()
		hh+=1



if __name__ == '__main__':
	Pattern_Programs(int(input()))