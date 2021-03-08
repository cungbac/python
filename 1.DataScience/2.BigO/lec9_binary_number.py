import sys
sys.setrecursionlimit(10000)

def binary(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return  str(binary(n//2)) + str(n%2)

n = int(input())
print(binary(n))