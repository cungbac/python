n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

m = [2,2]
# diagonal 1
temp1 = []
add = m[0] + m[1]
if add > n:
    i_1 = n-1
    j_1 = m[1]
    end1 = m[1]
elif add == n:
    i_1 = n - 1
    j_1 = 1
    end1 = 1
else:
    i_1 = add
    j_1 = 0
    end1 = 0

while i_1 >= end1:
    temp = a[i_1][j_1]
    temp1.append(temp)
    i_1 -= 1
    j_1 += 1

# diagonal 2
temp2 = []
minus = m[0] - m[1]
if minus < 0:
    i_2 = 0
    j_2 = abs(minus)
    end2 = n - abs(minus) - 1
else:
    i_2 = minus
    j_2 = 0
    end2 = n - 1

temp2 = []
while i_2 <= end2:
    temp = a[i_2][j_2]
    temp2.append(temp)
    i_2 += 1
    j_2 += 1

print(temp1)
print(temp2)