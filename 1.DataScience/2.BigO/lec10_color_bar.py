class color:
    def __init__(self,color_code,length):
        self.p = color_code
        self.l = length

class color_bar:
    def __init__(self,code,length=0,num=0):
        self.p = code
        self.l = length
        self.count = num

def insertionSort(a):
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

def get_unique_num(a):
    b = []
    for i in range(len(a)):
        if a[i].p not in b:
            b.append(a[i].p)
    return b
# Input & Output
n = int(input())

a = []
for i in range(n):
    p, l = map(int,input().split())
    a.append(color(p,l))


m = get_unique_num(a)
m = insertionSort(m)

b = []
for i in range(len(m)):
    b.append(color_bar(m[i]))

for i in range(len(a)):
    for j in range(len(b)):
        if a[i].p == b[j].p:
            b[j].l = b[j].l + a[i].l
            b[j].count = b[j].count + 1

print(len(b))
for i in range(len(b)):
    print(b[i].p,b[i].l,b[i].count)

