import sys
sys.setrecursionlimit(10000)

def sum_odd(a):
    n = len(a) - 1
    if n == 0:
        if a[0] % 2 == 0:
            return a[0]
        else: return 0
    temp = sum_odd(a[:n])
    if a[n] % 2 != 0:
        x = 0
        return x + temp
    else:
        return a[n] + temp
      
n = int(input())
for i in range(n):
    try:
        a = list(map(int,input().split()))
    except EOFError as e:
        print(end = '')

print(sum_odd(a))

