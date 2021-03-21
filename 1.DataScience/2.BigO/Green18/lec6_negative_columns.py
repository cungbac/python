m, n = map(int,input().split())

a = []
for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)

b = []
c = []
for j in range(n):
    for i in range(m):
        temp = a[i][j]
        if temp < 0:
            b.append(temp)
    c.append(b)
    b = []

for j in range(n):
    if len(c[j]) == m:
        print(j, end = ' ')

