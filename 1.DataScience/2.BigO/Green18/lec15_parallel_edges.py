n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

count = 0
mul = 1
for i in range(len(a)):
    if a[i][0] == a[i][1]:
        count += 1
        mul = mul * a[i][2]

result = mul % (10**6 +7)

if count == 0:
    print(-1)
else:
    print(count, result)