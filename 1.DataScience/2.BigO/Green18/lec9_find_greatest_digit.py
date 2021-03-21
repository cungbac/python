import sys
sys.setrecursionlimit(10000)

def max_num(n):
    n = abs(n)
    temp_max = n%10
    if n // 10 == 0:
        return n
    else:
        if max_num(n//10) > temp_max:
            return max_num(n//10)
        else:
            return temp_max
            

n = int(input())
print(max_num(n))