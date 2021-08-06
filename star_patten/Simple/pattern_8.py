def Pattern_Programs(n):
	str=1
	for i in range(1,n*2):
		print("*"*str)
		if i<n:
			str+=1
		else:
			str-=1


if __name__ == '__main__':
	Pattern_Programs(int(input()))