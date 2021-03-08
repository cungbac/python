# Input
m, n = map(int,input().split())
a = []

for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)

temp1 = []
x = 0
for i in range(m):
    for j in range(n):
        if a[i][j] % 2 == 0:
            x += 1
    temp1.append(x)
    x = 0

max = 0
for i in range(len(temp1)):
    if temp1[i] > max:
        max = temp1[i]
        index = i

print(index)