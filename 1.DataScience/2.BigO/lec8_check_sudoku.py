def transpose_list(a):
    """transpose 2D array"""
    temp1 = []
    temp2 = []
    for j in range(len(a)):
        for i in range(len(a)):
            x = a[i][j]
            temp1.append(x)
        temp2.append(temp1)
        temp1 = []
    return temp2

def get_sub_matrix(a):
    b = []
    c = []
    idx_i = 0
    idx_j = 0
    for idx_j in range(0,len(a),3):
        for idx_i in range(0,len(a),3):
            for i in range(idx_i, idx_i + 3):
                for j in range(idx_j, idx_j + 3):
                    temp = a[i][j]
                    b.append(temp)
            c.append(b)
            b = []
    return c

def check_sudoku_1(a):
    for i in range(9):
        for j in range(len(a[i])):
            for k in range(j+1,len(a[i])):
                if a[i][j] == a[i][k] or a[i][j] == 0:
                    return False
    return True

n = 9
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

transpose = transpose_list(a)
sub_matrix = get_sub_matrix(a)

if check_sudoku_1(a) and check_sudoku_1(transpose) and check_sudoku_1(sub_matrix):
    print('YES')
else:
    print('NO')