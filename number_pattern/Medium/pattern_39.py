def Pattern_Programs(n):
	counter=1
	for i in range(1,n+1):
		if i%2!=0:
			for j in range(i):
				print(counter,end=" ")
				counter+=1
		else:
			kk=counter+i-1
			for j in range(i):
				print(kk,end=" ")
				kk-=1
				counter+=1

		print()

if __name__ == '__main__':
	Pattern_Programs(int(input()))