# Class
class Employee:
    def __init__(self,code,name,year):
        self.code = code
        self.name = name
        self.birth_year = year
    
    def get_info(self):
        code = self.code
        name = self.name
        birth_year = self.birth_year
        return '{0} {1} {2}'.format(code,name,birth_year)

# Function
def get_employee(a):
    b = []
    for i in range(len(a)):
        code = a[i][0]
        name = a[i][1]
        birth_year = a[i][2]
        employee = Employee(code,name,birth_year)
        b.append(employee)
    return b

def get_max_year(a):
    max = 0
    for i in range(len(a)):
        year = int(a[i][2])
        if year > max:
            max = year
    return max 

def get_max_yearold(a):
    max = get_max_year(a)
    for i in range(len(a)):
        year = int(a[i][2])
        if year < max:
            max = year
    return max

def get_list_max(a):
    max_year = get_max_yearold(a)
    c = []
    for i in range(len(a)):
        year = int(a[i][2])
        if year == max_year:
            x = i
            c.append(x)
    return c

def get_idx(a):
    min = 9999999
    list_max_year = get_list_max(a)
    for idx in list_max_year:
        code = int(a[idx][0])
        if code < min:
            min = code
            x = idx
    return x

# Input & Output
n = int(input())
a = []
for i in range(n):
    temp = list(map(str,input().split()))
    a.append(temp)

employee_list = get_employee(a)
employee_show = get_idx(a)

print(employee_list[employee_show].get_info())


