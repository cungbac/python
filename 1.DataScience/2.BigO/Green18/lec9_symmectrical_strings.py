import sys
sys.setrecursionlimit(100000000)

def chuoidoixung(a,n):
    if n == 1:
        return a[0]
    else:
        func = chuoidoixung(a,n-1)
        temp = a[n-1]
        return temp + func

n = int(input())
try:
    a = input()
except EOFError:
    print(EOFError)
    
if a == chuoidoixung(a,n):
    print('YES')
else:
    print('NO')