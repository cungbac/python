def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

b = []
for i in range(len(a)):
    for j in range(len(a)):
        if j == len(a) - (i+1):
            temp = a[i][j]
            b.append(temp)

c = 1
for i in b:
    if isPrime(i):
        temp = i
        c = c * temp

print(c % 1000003)

