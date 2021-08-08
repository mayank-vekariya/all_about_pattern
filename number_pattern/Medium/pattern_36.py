def Pattern_Programs(n):
	spoint=1
	epoint=0
	for i in range(1,n+1):
		for j in range(spoint,n*2,2):
			print(j,end=" ")
		for k in range(1,epoint+1,2):
			print(k,end=" ")
		print()
		spoint+=2
		epoint+=2


if __name__ == '__main__':
	Pattern_Programs(int(input()))