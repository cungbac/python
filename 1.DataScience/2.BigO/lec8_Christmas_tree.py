n = int(input())

m = 1
for i in range(n):
    print(' '*(n-i-1)+'*'*m)
    m = m + 2