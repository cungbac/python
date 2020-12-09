def remove_zero(n):
    number = 0
    power10 = 1
    while n > 0:
        lastDigit = n % 10
        if lastDigit != 0:
            number = number + lastDigit * power10
            power10 = power10*10
        n = n // 10
    return number

n = int(input())
m = int(input())
sum_nm = n + m

if remove_zero(sum_nm) == remove_zero(n) + remove_zero(m):
    print('YES')
else:
    print('NO')