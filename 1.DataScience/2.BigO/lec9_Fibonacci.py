def fibonacci(a):
    if a == 0 or a == 1:
        return 1
    else:
        return fibonacci(a - 1) + fibonacci(a - 2)

n = int(input())
print(fibonacci(n))