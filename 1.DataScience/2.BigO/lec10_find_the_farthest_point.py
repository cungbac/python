
class Coordinate:
    def __init__(self,a=0,b=0):
        self.vertical = a
        self.horizontal = b
    
    def distance(self,p2):
        distance = ((self.vertical - p2.vertical)**2 + (self.horizontal - p2.horizontal)**2)**(1/2)
        return distance

a, b = map(int,input().split())
m = Coordinate(a,b)

n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

def get_max_point(a,m):
    max = 0
    for i in range(len(a)):
        point = Coordinate(a[i][0],a[i][1])
        temp = m.distance(point)
        if temp > max:
            max = temp
            x = i
            point_max = Coordinate(a[x][0],a[x][1])
    return point_max

point = get_max_point(a,m)
print(point.vertical, point.horizontal)

