
def merge(L,R):
    i = 0
    j = 0
    k = 0
    nL = len(L)
    nR = len(R)
    a = L + R
    while i < nL  and j < nR:
        if L[i] > R[j]:
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

def mergeSort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    else:
        nL = n // 2
        L = lst[:nL]

        nR = n - nL
        R = lst[nL:n]
        
        M = mergeSort(L)
        N = mergeSort(R)

        new = merge(M,N)

        return new

# Input and Output
n = int(input())
a = list(input().split())

for i in range(len(a)):
    a[i] = int(a[i])

a = mergeSort(a)

for i in range(len(a)):
    print(a[i],end = ' ')