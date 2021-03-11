n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

flag = True
for i in range(len(a)):
    for j in range(len(a[i])):
        # if i == j:
        #     if a[i][j] != 0:
        #         flag = False
        if a[i][j] != a[j][i]:
                flag = False

if flag:
    print('YES')
else:
    print('NO')