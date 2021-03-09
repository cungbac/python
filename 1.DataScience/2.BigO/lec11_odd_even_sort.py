
def insertionSort_Asc(a):
    if len(a) == 1:
        return a
    lst = [a[0]]
    for j in range(1,len(a)):
        lst.append(a[j])
        key = a[j]
        i = j
        while i >= 0:
            if i == 0:
                break
            if lst[i-1] <= key:
                break
            lst[i] = lst[i-1]
            i -= 1
        lst[i] = key
    return lst

def insertionSort_Desc(a):
    if len(a) == 1:
        return a
    lst = [a[0]]
    for j in range(1,len(a)):
        lst.append(a[j])
        key = a[j]
        i = j
        while i >= 0:
            if i == 0:
                break
            if lst[i-1] >= key:
                break
            lst[i] = lst[i-1]
            i -= 1
        lst[i] = key
    return lst

def insertionSort_odd_even(a):
    b = []
    idx_even = []
    c = []
    idx_odd = []

    for i in range(len(a)):
        if a[i] % 2 == 0:
            b.append(a[i])
            idx_even.append(i)
        else:
            c.append(a[i])
            idx_odd.append(i)

    if len(b) > 0:
        b = insertionSort_Asc(b)
        for i in range(len(idx_even)):
            a[idx_even[i]] = b[i] 
    if len(c) > 0:
        c = insertionSort_Desc(c)
        for i in range(len(idx_odd)):
            a[idx_odd[i]] = c[i]
    return a

# Input and Output
n = int(input())
a = list(input().split())
for i in range(len(a)):
    a[i] = int(a[i])

a = insertionSort_odd_even(a)

for i in a:
    print(i, end = ' ')