n, m = map(int,input().split())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

def insertionSort_Asc(a):
    if len(a) == 1:
        return a
    lst = [a[0]]
    for j in range(1,len(a)):
        lst.append(a[j])
        key = a[j][2]
        key2 = a[j]
        i = j
        while i >= 0:
            if i == 0:
                break
            if lst[i-1][2] <= key:
                break
            lst[i] = lst[i-1]
            i -= 1
        lst[i] = key2
    return lst

b = insertionSort_Asc(a)
c = []
for i in range(m):
    temp = [b[i][0],b[i][1]]
    c.append(temp)

x = len(c) - 1
while x >= 0:
    print(c[x][0],c[x][1])
    x -= 1