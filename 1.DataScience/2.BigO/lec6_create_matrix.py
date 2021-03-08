m, n = map(int,input().split())
a, b, p = map(int,input().split())

x = []
y = []
z = []
temp1 = a
temp2 = b
result = []
    
for i in range(n):
    for j in range(m):
        x.append(temp1)
        temp = temp1 + temp2
        temp1 = temp2
        temp2 = temp % p

for i in range(1,m+1):
    for j in range(n*(i-1),n*i):
        y.append(x[j])
    result.append(y)
    y = []

for val in result:
    for i in range(len(val)):
        print(val[i], end = ' ')
    print() 

