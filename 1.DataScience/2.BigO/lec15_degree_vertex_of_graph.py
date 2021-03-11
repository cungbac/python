n, m = map(int,input().split())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

b = a[m]
sum = 0
for i in range(len(b)):
    sum = sum + b[i]

print(sum)