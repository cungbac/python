class apple:
    def __init__(self, weight=0, price=0):
        self.weight = weight
        self.price = price
    
# Input & Out Put
n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

def get_max_weight(a):
    max =  0
    for i in range(len(a)):
        weight = a[i][0]
        if weight > max:
            max = weight
    return max

def get_max_price(a):
    max =  0
    for i in range(len(a)):
        price = a[i][1]
        if price > max:
            max = price
    return max

b = []
for i in range(len(a)):
    if a[i][0] == get_max_weight(a):
        x = i
        b.append(x)

c = []
for idx in b:
    c.append(a[idx])

for idx in b:
    if a[idx][1] == get_max_price(c):
        x = idx

print(x)

