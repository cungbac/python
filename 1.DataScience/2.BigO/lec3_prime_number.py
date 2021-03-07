n = int(input())
s = 0

for i in range(2,n):
    if n % i == 0:
        s += 1

if n == 1:
    print('NO')
else:
    if s == 0:
        print('YES')
    else:
        print('NO')

