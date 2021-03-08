n = int(input())
a = list(map(int,input().split()))

x = 0
y = 0
end = 'YES'
for i in range(n):
    if a[-1] == 0:
        end = 'NO'
    if a[i] == 1:
        y = 0
        x = y
    if a[i] == 0:
        x += 1
        if x > 3:
            end = 'NO'
            break
print(end)