def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

a = int(input())
i = 1
total = 0
while i < a:
    if a <= 2:
        total = 0
    elif isPrime(i) == True:
        total = total + i
    i += 1
print(total)