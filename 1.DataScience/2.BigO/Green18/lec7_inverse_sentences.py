a = input()

b = a.split()

m = len(b)
c = []
while m > 0:
    m -= 1
    c.append(b[m])

text = ''
for i in range(len(c)):
    if i == 0:
        text = text + c[i]
    else:
        text = text + ' ' + c[i]

print(text)