max = -1
min = 11
while True:
    x = int(input())
    if x == -1:
        break
    if x > max:
        max = x
    if x < min: 
        min = x
print(max, min, end = ' ')