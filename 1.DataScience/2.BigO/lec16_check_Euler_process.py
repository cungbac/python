n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)
b = []
for i in range(n):
    count = 0
    for j in range(n):
        if a[i][j] == 1:
            count += 1
    b.append(count)

flag = True
for i in range(len(b)):
    if b[i] <= 1 or b[i] % 2 != 0 :
        flag = False

if flag:
    print('YES')
else:
    print('NO')
    