n = int(input())

a = list(map(int,input().split()))

x = 0
for i in range(n):
  x = x + a[i]
print(x)