# 2D array
# a = [10,20,30,40]
# b = [40,50,60,70]
# c = [4,5,6,8]
# e = [8,0,9,7]

# d = []
# d.append(a)
# d.append(b)
# d.append(c)
# d.append(e)

# for i in range(len(d)):
#     for j in range(len(d[i])):
#         print(d[i][j])

# for i in range(len(d)):
#     for j in range(len(d[i])):
#         print(d[j][i])

# n = int(input())
# a = list(map(int,input().split()))

# bai 1 - tinh tong
# m, n = map(int,input().split())

# a = []
# for i in range(m):
#   temp = list(map(int,input().split()))
#   a.append(temp)

# sum = 0
# for i in range(m):
#     for j in range(n):
#         sum = sum + a[i][j]
#     print(str(i) + ': ' + str(sum))
#     sum = 0 

# bai 2 - cot toan am
# m, n = map(int,input().split())

# a = []
# for i in range(m):
#     temp = list(map(int,input().split()))
#     a.append(temp)

# b = []
# c = []
# for j in range(n):
#     for i in range(m):
#         temp = a[i][j]
#         if temp < 0:
#             b.append(temp)
#     c.append(b)
#     b = []

# for j in range(m):
#     if len(c[j]) == n:
#         print(j, end = ' ')

# # bai 3 - dem so nguyen to tren bien
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# m, n = map(int,input().split())
# a = []
# for i in range(m):
#     temp = list(map(int,input().split()))
#     a.append(temp)

# y = 0
# for j in range(n):
#     for i in range(-1,0):
#         if isPrime(a[i][j]):
#             y += 1
# x = 0
# for i in range(m):
#     for j in range(1,n-1,n-2):
#         if isPrime(a[i][j]):
#             x += 1

# print(x+y)

# # bai 4 - dem so nguyen tren duong cheo
# n = int(input())
# a = []
# for i in range(n):
#     temp = list(map(int,input().split()))
#     a.append(temp)

# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# x = 0
# for i in range(n):
#     for j in range(n):
#         if i == j and isPrime(a[i][j]):
#             x += 1

# print(x)

# # bai 6 - tim dong nhieu so chan nhat
# # Input
# m, n = map(int,input().split())
# a = []

# for i in range(m):
#     temp = list(map(int,input().split()))
#     a.append(temp)

# temp1 = []
# x = 0
# for i in range(m):
#     for j in range(n):
#         if a[i][j] % 2 == 0:
#             x += 1
#     temp1.append(x)
#     x = 0

# max = 0
# for i in range(len(temp1)):
#     if temp1[i] > max:
#         max = temp1[i]
#         index = i

# print(index)

# # bai 7 - dem anh
# # Input
# m, n = map(int,input().split())
# a = []
# for i in range(m):
#     temp = list(map(int,input().split()))
#     a.append(temp)

# # Code
# x = 0
# for i in range(m):
#     for j in range(n):
#         if a[i][j] > 100:
#             x += 1

# print(x)

# dem so hoang hau

n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

def get_column(a):
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

a_by_column = get_column(a)

def get_max(a):
    """get max of a row in a 2D array"""
    max = 0
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    return max

# get the list of max in both row and column
list_max = []
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][j] == get_max(a[i]) and a[i][j] == get_max(a_by_column[j]):
            x = a[i][j]
            list_max.append(x)

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

print(list_max)
print(diagonal_1)
