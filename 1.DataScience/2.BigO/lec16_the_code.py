a = input()
b = ''
c = ''
for i in range(len(a)):
    if i % 2 == 0:
        b = b + a[i]
    else:
        c = c + a[i]

def inverse_string(a,n):
    if n == 0:
        return ''
    else:
        return a[n-1] + inverse_string(a,n-1)

c = inverse_string(c,len(c))

e = ''
i = len(b)
j = len(c)

if len(a) % 2 == 0:
    for i in range(len(c)):
        e = e + b[i] + c[i]
else:
    for i in range(len(c)):
        e = e + b[i] + c[i]
    e = e + b[len(b) - 1]

print(e)