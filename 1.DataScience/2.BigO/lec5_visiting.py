n = int(input())
a = list(map(int,input().split()))

x = 0
y = 0
for i in range(n):
    if a[i] == 0:
        x += 1
    elif a[i] == 1:
        y += 1

if x == y:
    print('YES')
else:
    print('NO')