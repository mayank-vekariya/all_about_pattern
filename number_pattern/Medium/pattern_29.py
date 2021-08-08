def Pattern_Programs(n):
	for i in range(1,n+1):
		print("*"*i)


if __name__ == '__main__':
	Pattern_Programs(int(input()))

# for (int i = 0; i < rows; i++)
# 	{
# 	for (int j = 0; j <= i; j++)
# 	{
# 	if (j % 2 == 0)
# 	{
# 	System.out.print(1 + j * rows - (j - 1) * j / 2 + i - j + " ");
# 	} else
# 	{
# 	System.out.print(1 + j * rows - (j - 1) * j / 2 + rows - 1 - i + " ");
# 	}
# 	}
#
# 	System.out.println();
# 	}