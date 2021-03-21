import sys
sys.setrecursionlimit(10000)

def count_number(a):
    if abs(a) // 10 == 0:
        return 1
    else:
        return 1 + count_number(abs(a)//10)

n = int(input())
print(count_number(n))