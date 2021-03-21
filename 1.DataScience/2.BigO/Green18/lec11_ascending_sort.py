def insertionAsc(a,n,x):
    j = n
    a.append(x)
    while j >= 0:
        if j == 0:
            break
        if a[j-1] <= x:
            break
        a[j] = a[j-1]
        j -= 1
    a[j] = x
    return a

def insertionSort(a):
    m = len(a)
    if m == 1:
        return a[0]
    for i in range(1,len(a)):
        x = a[i]
        b = insertionAsc(a,i,x)    
    c = b[:m]
    return c


# Input & Output
n = int(input())
a = []
a.append(input().split())
a = a[0]
for i in range(len(a)):
    a[i] = int(a[i])

c = insertionSort(a)
if len(a) == 1:
    print(a[0])
else:
    for i in c:
        print(i, end = ' ')