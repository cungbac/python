a = []
for i in range(4):
    temp = list(map(int,input().split()))
    a.append(temp)

flag = False
for i in range(len(a)):
    if a[i][3] == 1:
        if a[i][0] == 1 or a[i][1] == 1 or a[i][2] == 1:
            flag = True

if a[0][3] == 1 and (a[1][0] == 1 or a[2][1] == 1 or a[3][2] == 1):
    flag = True

if a[1][3] == 1 and (a[2][0] == 1 or a[3][1] == 1 or a[0][2] == 1):
    flag = True

if a[2][3] == 1 and (a[3][0] == 1 or a[0][1] == 1 or a[1][2] == 1):
    flag = True

if a[3][3] == 1 and (a[0][0] == 1 or a[1][1] == 1 or a[2][2] == 1):
    flag = True

if flag:
    print('YES')
else:
    print('NO')