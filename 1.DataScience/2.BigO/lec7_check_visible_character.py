n = input()

a = ['B','I','G','O']
flag = False
for i in a:
    if n.lower().find(i.lower()) >= 0:
        flag = True
if flag:
  print('YES')
else:
  print('NO')