n = int(input())
a = list(map(int,input().split()))

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


x = 0
for i in range(n):
    if isPrime(a[i]):
        x += 1
print(x)

