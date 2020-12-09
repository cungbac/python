
# USER DEFINED FUNCTION

# Tim so nguyen to gan nhat - nearest prime

a = 5
b = 10
c = add(a + b)


def add(num1, num2):
    num3 = num1 + num2
    return num3

add(1,2) + add(4,5)
add('3','12')

# 1
def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

a = 3
i = 1
total = 0
while i < a:
    if a <= 2:
        total = 0
    elif isPrime(i) == True:
        total = total + i
    i += 1
    
print(total)

# 2
def sqrt_1(n):
    n2 = n**2
    return int(n2)

sqrt_1(5)

a = 5 
b = 0
for i in range(1,a+1):
    b += sqrt_1(i)

print(b)

# 3 - greatest common division UCLN

def gcm(n,m):
    i = 0
    cont = 0
    while i <= m:
        i += 1
        if n % i == 0 and m % i == 0:
            if i > cont:
                cont = i
    return cont

print(int(2/gcm(2,4)),int(4/gcm(2,4)))


# 4 - Dem so luong chu so

n = int(input())
def count_num(n):
    i = 0
    while n > 0:
        i += 1
        n = n // 10
    return i

count_num(9999)

# 5 - Chu so lon nhat
def greatest_num(n):
    max = 0
    while n > 0:
        digit = n % 10
        if digit > max:
            max = digit
        n = n // 10
    return max

print(greatest_num(125))

# 6 Tim so nguyen to gan N nhat

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

nearest_prime(10)

# 7 Kiem tra doi xung

def newnum(n):
    num = 0
    while n > 0:
        digit = n % 10
        num = int(str(num) + str(digit))
        n = n // 10
    return num

def check(n):
    if n == newnum(n):
        return "YES"
    else:
        return 'NO'

check(12344321)

# codeforces - System of Equations

i = 0
n = 14
m = 28
a = 0
max = 0
running = True
while running:
    a += 1
    if (m - n**2) == (a ** 4 - 2 *( a**2) * n + a):
        i += 1
        running = False

    
print(i)
print(a)
print(b)
