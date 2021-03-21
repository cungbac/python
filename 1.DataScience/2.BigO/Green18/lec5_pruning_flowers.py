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

print(x)