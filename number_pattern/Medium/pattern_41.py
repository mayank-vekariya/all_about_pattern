def Pattern_Programs(n):
	point=1
	space=-1
	for i in range(1,n+1):
		if i==1:
			kk=n
			for j in range(1,n*2):
				print(kk,end="")
				if j<n:
					kk-=1
				else:
					kk+=1
		else:
			for j in range(n, point - 1, -1):
				print(j, end="")
			for _ in range(space):
				print(" ", end="")
			for k in range(point, n + 1):
				print(k, end="")
		print()
		point+=1
		space+=2



if __name__ == '__main__':
	Pattern_Programs(int(input()))