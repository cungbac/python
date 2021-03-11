n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

m = a[0][2]
for i in range(len(a)):
    if a[i][2] < m:
        m = a[i][2]

sum = 0
for i in range(len(a)):
    if a[i][2] == m:
        sum = sum + a[i][2]

print(sum)