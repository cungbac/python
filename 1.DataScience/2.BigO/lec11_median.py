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
        return a
    for i in range(1,m):
        x = a[i]
        b = insertionAsc(a,i,x)
    c = b[:m]
    return c

# Input and Output
n = int(input())
a = list(input().split())
for i in range(n):
    a[i] = int(a[i])
a = insertionSort(a)

m = len(a)
if m % 2 != 0:
    print(a[m//2])
else:
    x = (a[int(m/2)-1] + a[int(m/2)])/2
    print(round(x,1))


