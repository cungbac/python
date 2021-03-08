import sys
sys.setrecursionlimit(10000)

def max_divisor(n):
    temp = n%2
    if n <= 2:
        return 1
    if n%2 != 0:
        return int(n)
    else:
        return int(max_divisor(n/2))

n = int(input())
print(max_divisor(n))