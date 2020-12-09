
# LOOP

def sum(n):
    anw = 0
    for i in range(1,n):
        anw += i
    return anw

n = int(input())
ans = 0

def sum(n):
    for i in range(1,n+1,1):
        ans += i

print(sum(n))

# range; [begin, end)

# debug
n = int(input())
ans = 0

for i in range(5,1,-1): #only accept int
    ans += i
    print(i)

while i <= 5:
    ans += i
    i = i + 1
    print(ans)

# while
n = 12345
while n > 0:
    digit = n % 10
    print(digit, end = ' ')
    n = n // 10

# break: stop/exit the loop if meet conditions
for i in range(1 , 10):
    if i % 2 == 0:
        break
    print(i)

# continue: ignore action, still loop
for i in range(1,10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1,10):
    if i % 2 != 0:
        print(i)

for i in range(1,10,2):
    print(i)

# read n integers
n = int(input())
for i in range (1,n+1,1):
    x = int(input())


while 10 < 13:
    x = int(input())
    if x == 0:
        break
# tinh min / max
max = 0 
n = int(input())
for i in range(n):
    x = int(input())
    if x > max:
        max = x
print(max)

# flag
flag = True # gia su gia dinh dung
n = int(input())
for i in range(n):
    x = int(input())
    if x % 3 != 0:
        flag = False
if flag:
    print('Yes')
else:
    print('No')

# 1
n = int(input())
s = 0
for i in range(1,n+1):
  s += i
print(s)

# 2
s = 0
while True:
    x = int(input())
    if x == 0:
        break
    if x == 5:
        s += 1
print(s)

# 3 
max = -1
min = 11
while True:
    x = int(input())
    if x == -1:
        break
    if x > max:
        max = x
    if x < min: 
        min = x
print(max, min, end = ' ')

# 4
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

# 5 - Day tang
temporary = 1000000
s = 0
while True:
    x = float(input())
    if x == 0:
        break
    if x < temporary:
        temporary = x
        s += 1

if s == 1:
    print('YES')
else:
    print('NO')

# 6 - Chia keo

n = int(input())
s = 0
for i in range(n):
    x = int(input())
    if x % 2 != 0:
        s += 1

if s > 0:
    print('NO')
else:
    print('YES')

# 7 - Hang rao
n = int(input())
n = 6
print('*' * n)
for i in range(1,n-1):
    print('*',(n-3)*' '+'*')
print('*' * n)

# A.Tram
n = int(input())
capacity = 0
max = 0

for i in range(n):
    train_out, train_in = map(int,input().split())
    capacity = capacity + train_in - train_out

# A. Vanya and Cubes
i = 0
n = int(input())
cubes = 0
total = 0

n = 25
while total <= n:
    i += 1
    cubes = cubes + i
    total = total + cubes

print(i - 1)

for i in range(1,5):
    cubes += i
    total = total + cubes
    print(str(cubes) + ' - ' + str(total))

