def Pattern_Programs(n):
	isp=0
	for i in range(1,n+1):
		if i==1:
			print("*")
		elif i==n:
			print("*"*n)
		else:
			print("*"+" "*isp+"*")
			isp+=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))