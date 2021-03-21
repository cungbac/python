n = int(input())
a = list(map(int,input().split()))

flag = True
for i in range(n):
  if a[i] == 0:
    flag = False
if flag:
  print('YES')
else:
  print('NO')

