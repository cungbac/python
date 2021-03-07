temporary = 1000000
s = 0
while True:
    x = float(input())
    if x == 0:
        break
    if x < temporary:
        temporary = x
        s += 1

if s == 1:
    print('YES')
else:
    print('NO')

    
    
    