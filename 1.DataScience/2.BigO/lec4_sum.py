def sqrt_1(n):
    n2 = n**2
    return int(n2)

a = int(input())
b = 0
for i in range(1,a+1):
    b += sqrt_1(i)
print(b)