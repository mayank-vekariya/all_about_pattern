def Pattern_Programs(n):
    for i in range(n, 0, -1):
        print(" "*(n - i) + "*"*i)


if __name__ == '__main__':
    Pattern_Programs(int(input()))
