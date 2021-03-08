a = input()

b = a.split()
m = ''
c = []
for i in range(len(b)):
    for j in range(len(b[i])):
        if j == 0:
            m = b[i][j]
    c.append(m)
    m = ''

n = ''
for i in c:
    n = n+i
print(n.upper())