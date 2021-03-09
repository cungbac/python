class cell:
    def __init__(self,x,y,val = None):
        self.x = x
        self.y = y
        self.val = val

m, n = map(int,input().split())
k = int(input())

a = []
for i in range(k):
    x, y, val = map(int,input().split())
    a.append(cell(x,y,val))

lst = [x for x in a if x.val > 0]

print(len(lst))
for i in range(len(lst)):
    print(lst[i].x, lst[i].y)