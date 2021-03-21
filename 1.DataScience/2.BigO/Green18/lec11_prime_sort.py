def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def mergeSort_Asc(lst):
    def merge(L,R):
        i = 0
        j = 0
        k = 0
        nL = len(L)
        nR = len(R)
        a = L + R
        while i < nL  and j < nR:
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        
        while i < nL and j == nR:
            a[k] = L[i]
            i += 1
            k += 1
        
        while j < nR and i == nL:
            a[k] = R[j]
            j += 1
            k += 1
        return a

    n = len(lst)
    if n <= 1:
        return lst

    else:
        nL = n // 2
        L = lst[:nL]

        nR = n - nL
        R = lst[nL:n]
        
        M = mergeSort_Asc(L)
        N = mergeSort_Asc(R)

        new = merge(M,N)
        return new

def sort_notPrime(a):
    b = []
    idx_Prime = []

    c = []
    idx_notPrime = []


    for i in range(len(a)):
        if a[i] < 0:
            c.append(a[i])
            idx_notPrime.append(i)
        else:
            if isPrime(a[i]):
                b.append(a[i])
                idx_Prime.append(i)
            else:
                c.append(a[i])
                idx_notPrime.append(i)

    c = mergeSort_Asc(c)

    for i in range(len(idx_Prime)):
        a[idx_Prime[i]] = b[i]
    for i in range(len(idx_notPrime)):
        a[idx_notPrime[i]] = c[i]
    
    return a

# Input & Output
n = int(input())
a = list(input().split())
for i in range(n):
    a[i] = int(a[i])

a = sort_notPrime(a)

for i in range(len(a)):
    print(a[i],end = ' ')


