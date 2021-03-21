n, m = map(int,input().split())

a = input().split()
count = 0
for i in range(len(a)):
    if int(a[i]) == m:
        temp = i + 1
        count += 1

if count > 0:
    print(temp)
else:
    print(-1)


