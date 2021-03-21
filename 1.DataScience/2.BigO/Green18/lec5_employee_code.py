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