# Theater square

n, m, a = map(int(input().split()))

if n % a == 0:
    x = int(n/a)
else:
    x = int(n/a + 1)

if m % a == 0:
    y = int(m/a)
else:
    y = int(m/a) + 1

print(x * y)


