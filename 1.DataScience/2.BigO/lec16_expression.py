m = int(input())
n = int(input())
k = int(input())

a = m + n + k
b = m*n + k
c = m + n*k
d = (m+n)*k
e = m*(n+k)
f = m*n*k

lst = [a,b,c,d,e,f]

max = lst[0]
for i in range(len(lst)):
    if lst[i] > max:
        max = lst[i]

print(max)