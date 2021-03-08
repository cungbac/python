n = int(input())
a = []
for i in range(n):
    temp = input()
    a.append(temp)

m = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i] != a[j]:
            m += 1
            # print(str(a[i]) + '-' + str(a[j]))
        break

if m > 0:
    print(m + 1)
else:
    print(m)