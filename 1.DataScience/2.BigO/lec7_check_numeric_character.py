a = input()
b = ''
for i in range(len(a)):
    if ord(a[i]) >= 48 and ord(a[i]) <=57:
        b = b + a[i]
print(len(b))