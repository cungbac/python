
def equation(n,m):
    running = True
    i = 0
    a = 0
    while running:
        if (m - n**2) == (a ** 4 - 2 *( a**2) * n + a):
            i += 1
            running = False
        else:
            a += 1
            continue
    return i

n, m = map(int,input().split())
print(equation(n, m))

equation(4,20)
equation(14,28)