def Pattern_Programs(n):
	insp=0
	for i in range(1,n*2):
		if i==n*2-1 or i==1:
			print("*")
		else:
			print("*"+" "*insp+"*")
			if i<n:
				insp+=1
			else:
				insp-=1
if __name__ == '__main__':
	Pattern_Programs(int(input()))