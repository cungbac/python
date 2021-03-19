def get_inverse(a,n):
    if n == 1:
        return a[0]
    else:
        m = a[n-1]
        func = get_inverse(a,n-1)
        return m + func

def check_doixung(a):
    inverse = get_inverse(a,len(a))
    if a == inverse:
        return 'YES'
    else:
        return 'NO'

# Iput and Output
n = int(input())
a = input()
print(check_doixung(a))