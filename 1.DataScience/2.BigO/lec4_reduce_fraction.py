a, b = map(int,input().split())

def gcm(n,m):
    i = 0
    cont = 0
    while i <= m:
        i += 1
        if n % i == 0 and m % i == 0:
            if i > cont:
                cont = i
    return cont

print(int(a/gcm(a,b)), int(b/gcm(a,b)))

