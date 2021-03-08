a = int(input())

def greatest_num(n):
    max = 0
    while n > 0:
        digit = n % 10
        if digit > max:
            max = digit
        n = n // 10
    return max
print(greatest_num(a))