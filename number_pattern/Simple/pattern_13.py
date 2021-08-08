def Pattern_Programs(n):

	osp=n-1
	for i in range(1,n+1):
		print(" "*osp,end="")
		hh=1
		for j in range(1,i+1):
			print(hh,end=" ")
			hh=int(hh*(i-j)/j)
		osp-=1
		print()
if __name__ == '__main__':
	Pattern_Programs(int(input()))