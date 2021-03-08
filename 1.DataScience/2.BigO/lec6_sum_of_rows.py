m, n = map(int,input().split())

a = []
for i in range(m):
  temp = list(map(int,input().split()))
  a.append(temp)

sum = 0
for i in range(m):
    for j in range(n):
        sum = sum + a[i][j]
    print(str(i) + ': ' + str(sum))
    sum = 0 