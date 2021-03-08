m, n = map(int,input().split())
a = []
for i in range(m):
    temp = list(map(int,input().split()))
    a.append(temp)

def max_row_col(a,m,n,row,col):
    for i in range(m):
        if a[i][col] < a[row][col]:
            return False
    
    for j in range(n):
        if a[row][j] > a[row][col]:
            return False
    return True

count = 0
for i in range(m):
    for j in range(n):
        if max_row_col(a,m,n,i,j):
            count += 1

print(count)