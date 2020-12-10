n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)


# diagonal_1
diagonal_1 = []
for i in range(n):
    for j in range(n):
        if i == j:
            diagonal_1.append(a[i][j])
# diagonal_2
diagonal_2 = []
for i in range(n):
    for j in range(n):
        if i == n - (j+1):
            diagonal_2.append(a[i][j])

x = 0
for i in range(len(list_max)):
    if list_max[i] in diagonal_1 or list_max[i] in diagonal_2:
        x += 1