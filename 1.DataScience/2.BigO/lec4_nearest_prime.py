def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def nearest_prime(n):
    ans = 0
    n1 = n
    n2 = n
    while True:
        if isPrime(n1) == True:
            ans = n1
            return ans
            break
        n1 -= 1

        if isPrime(n2) == True:
            ans = n2
            return ans
            break
        n2 += 1
a = int(input())
print(nearest_prime(a))