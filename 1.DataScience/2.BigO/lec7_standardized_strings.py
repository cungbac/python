n = input()

a = n.split(' ')
b = []
for i in range(len(a)):
  if a[i] != '':
    x = a[i]
    b.append(x)
c = ''
for i in range(len(b)):
  if i == 0:
    c = c + b[i]
  else:
    c = c + ' ' + b[i]
    
print(c)