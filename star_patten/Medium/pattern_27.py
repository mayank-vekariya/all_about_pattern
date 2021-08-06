def Pattern_Programs(n):
	insp=0
	star=n
	for i in range(1,n*2):
		print("*" * star + " " * insp + "*" * star)
		if i < n:
			star -= 1
			insp += 2
		else:
			star += 1
			insp -= 2


if __name__ == '__main__':
	Pattern_Programs(int(input()))