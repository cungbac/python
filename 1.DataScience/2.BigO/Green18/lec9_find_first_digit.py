import sys
sys.setrecursionlimit(10000)

def get_first_number(n):
    temp = abs(n) // 10
    if abs(n) // 10 == 0:
        return abs(n)
    else:
        return 0 + get_first_number(temp)

n = int(input())
print(get_first_number(n))