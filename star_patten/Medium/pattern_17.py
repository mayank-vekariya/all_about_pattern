def Pattern_Programs(n):
	insp=n-3
	for i in range(1,n+1):
		if i == n:
			print("*")
		elif i == 1:
			print("*" * n)
		else:
			print("*" + " " * insp + "*")
			insp -= 1



if __name__ == '__main__':
	Pattern_Programs(int(input()))