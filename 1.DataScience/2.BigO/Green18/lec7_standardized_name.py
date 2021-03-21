n = int(input())
a = []
for i in range(n):
    temp = input()
    a.append(temp)

def manipulate_text(a):
    b = ''
    c = []
    for i in range(len(a)):
        for j in range(len(a[i])):
            if j == 0:
                b = b + a[i][j].upper()
            else:
                b = b + a[i][j].lower()
        c.append(b)
        b = ''
    text = ''
    for i in range(len(c)):
        if i == 0:
            text = text + c[i]
        else:
            text = text + ' ' + c[i]
    return text

m = []
for i in range(len(a)):
    b = a[i].split(' ')
    m.append(b)

for string in m:
    print(manipulate_text(string))