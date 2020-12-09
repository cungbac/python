n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

m = [2,0]

# diagonal 1
temp1 = []
y = 0
x = m[0] + m[1]
while x >= 0:
    temp = a[x][y]
    temp1.append(temp)
    x -= 1
    y += 1

# diagonal 1
temp2 = []
y = 0
x = abs(m[0] - m[1])
while x >= 0:
    temp = a[x][y]
    temp2.append(temp)
    x -= 1
    y += 1


print(temp1)
