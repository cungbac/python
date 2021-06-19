from itertools import permutations

lst = input().split()

n = int(lst[1])
a = list(lst[0])

b = list(permutations(a,n))
b = sorted(b,key=lambda x: [x[0],x[1]])

for i in b:
    print(''.join(i))
