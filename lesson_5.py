def foo1(x):
    x +=1
    return x

a = 10
print(fool1(a))

'a, x: int => primitive type => pass by value'

# 4
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

# Tia hoa
n = int(input())
a = list(map(int,input().split()))

def find_max(a):
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

def find_min(a):
    min = find_max(a)
    for i in range(len(a)):
        if a[i] < min:
            min = a[i]
    return min

x = 0
y = find_min(a)
for i in range(n):
    if a[i] > y:
        diff = a[i] - y
        x = x + diff

# Tham quan
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

# Ma so nhan vien
n = int(input())
a = list(map(int,input().split()))

def sort_list(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[j] < a[i]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a

a = sort_list(a)
x = 0
s = 0
for i in range(len(a)):
    if a[0] != 1:
        s = 1
    if a[i] == x + 1:
        x = a[i]
        s = x + 1
    else:
        break

print(s)

# Trai cay
# input
n = int(input())
the_list = []

for i in range(n):
    x = list(map(int,input().split()))
    the_list.append(x)

# get max
def get_max_tao(a):
    max = 0
    for i in range(len(a)):
        if a[i][0] > max:
            max = a[i][0]
    return max
max_tao = get_max_tao(the_list)

def get_max_cam(a):
    max = 0
    for i in range(len(a)):
        if a[i][0] == max_tao and a[i][1] > max:
            max = a[i][1]
            x = i
    return max
max_cam = get_max_cam(the_list)

def count_max(a):
    x = 0
    for i in range(len(a)):
        if a[i][0] == max_tao:
            x += 1
    return x

no_of_max = count_max(the_list)

for i in range(n):
    if the_list[i][0] == max_tao and the_list[i][1] == max_cam:
        index = i + 1
    elif the_list[i][0] == max_tao:
        index = i + 1
        break

print(index)

# Quan ly LaLa
n = int(input())
a = list(map(int,input().split()))

x = 0
y = 0
end = 'YES'
for i in range(n):
    if a[-1] == 0:
        end = 'NO'
    if a[i] == 1:
        y = 0
        x = y
    if a[i] == 0:
        x += 1
        if x > 3:
            end = 'NO'
            break

print(end)
