def newnum(n):
    num = 0
    while n > 0:
        digit = n % 10
        num = int(str(num) + str(digit))
        n = n // 10
    return num

def check(n):
    if n == newnum(n):
        return 'YES'
    else:
        return 'NO'
n = int(input())
print(check(n))
      