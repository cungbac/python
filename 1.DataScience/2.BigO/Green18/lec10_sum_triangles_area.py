
# Class
class Coordinate:
    def __init__(self,vertical = 0, horizontal = 0):
        self.vertical = vertical
        self.horizontal = horizontal

class triangle:
    p1 = Coordinate()
    p2 = Coordinate()
    p3 = Coordinate()
    def __init__(self,p1,p2,p3):
        self.point_1 = p1
        self.point_2 = p2
        self.point_3 = p3

    def triangle_area(self):
        a = ((self.point_1.vertical - self.point_2.vertical)**2 + (self.point_1.horizontal - self.point_2.horizontal)**2)**(1/2)
        b = ((self.point_1.vertical - self.point_3.vertical)**2 + (self.point_1.horizontal - self.point_3.horizontal)**2)**(1/2)
        c = ((self.point_2.vertical - self.point_3.vertical)**2 + (self.point_2.horizontal - self.point_3.horizontal)**2)**(1/2)
        half_perimeter = (a+b+c)/2
        area = (half_perimeter*(half_perimeter-a)*(half_perimeter-b)*(half_perimeter-c))**(1/2)
        return area

# Function
def get_area(a):
    b = []
    for i in range(len(a)):
        if (i+1) % 3 == 0:
            b.append(a[i-2:i+1])

    c = []
    d = []
    for i in range(len(b)):
        for j in range(len(b[i])):
            vertical = float(b[i][j][:b[i][j].find(' ')])
            horizontal = float(b[i][j][b[i][j].find(' ')+1:])
            point = Coordinate(vertical,horizontal)
            c.append(point)
        d.append(c)
        c = []
    
    x = float(0)
    for i in range(len(d)):
        p1 = d[i][0]
        p2 = d[i][1]
        p3 = d[i][2]
        point = triangle(p1,p2,p3)
        area = triangle.triangle_area(point)
        x = x + area
    return '{:.2f}'.format(x)

# Input & Output
n = int(input())
a = []
for i in range(n*3):
    temp = input()
    a.append(temp)

x = get_area(a)
print(x)