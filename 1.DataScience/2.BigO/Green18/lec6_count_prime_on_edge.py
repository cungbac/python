# Dem so nguyen to tren bien

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

m, n = map(int,input().split())
a = []
for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)

y = 0
for j in range(n):
    for i in range(-1,1):
        if isPrime(a[i][j]):
            y += 1
x = 0
if n > 2:
    for i in range(1,m-1):
        for j in range(-1,1):
            if isPrime(a[i][j]):
                x += 1
print(x + y)