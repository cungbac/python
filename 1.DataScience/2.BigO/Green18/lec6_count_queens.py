# m, n = map(int,input().split())
n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)


def max_in_direction(a,n,row,col,x,y):
    i = row
    j = col
    while 0 <= i < n and 0 <= j < n:
        if a[i][j] > a[row][col]:
            return False
        i = i + x
        j = j + y
    return True


def is_queen(a,n,row,col):
    for i in range(n):
        if a[i][col] > a[row][col]:
            return False
    
    for j in range(n):
        if a[row][j] > a[row][col]:
            return False
    
    dir_1 = max_in_direction(a,n,row,col,1,1)
    dir_2 = max_in_direction(a,n,row,col,1,-1)
    dir_3 = max_in_direction(a,n,row,col,-1,1)
    dir_4 = max_in_direction(a,n,row,col,-1,-1)

    return dir_1 and dir_2 and dir_3 and dir_4


count = 0
for i in range(n):
    for j in range(n):
        if is_queen(a,n,i,j):
            count += 1

print(count)