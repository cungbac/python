n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

x = 0
for i in range(n):
    for j in range(n):
        if i == j and isPrime(a[i][j]):
            x += 1

print(x)