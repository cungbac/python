import sys
sys.setrecursionlimit(10000)

def hexadecimal(n):
    num = n%16
    if int(n%16) == 10:
        num = 'A' 
    elif int(n%16) == 11:
        num = 'B'
    elif int(n%16) == 12:
        num = 'C'
    elif int(n%16) == 13:
        num = 'D'
    elif int(n%16) == 14:
        num = 'E'
    elif int(n%16) == 15:
        num = 'F'
    else:
        num = str(n%16)
    if n < 16:
        return num
    else:
        func = str(hexadecimal(n//16))
        return func + num

n = int(input())
n = hexadecimal(n)

print(n)