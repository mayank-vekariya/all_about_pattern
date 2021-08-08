def Pattern_Programs(n):
	space=n-1
	for i in range(1,n*2,2):
		print(" "*space,end="")
		temp=1
		for j in range(1,i+1):
			print(temp,end="")
			if j<=i//2:
				temp+=1
			else:
				temp-=1
		space-=1
		print()



if __name__ == '__main__':
	Pattern_Programs(int(input()))