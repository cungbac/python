class Student:
    def __init__(self,std_code,math,literature):
        self.std_code = str(std_code)
        self.score_math = math
        self.score_literature = literature
    
    def get_score(self):
        score_math = self.score_math
        score_literatue = self.score_literature
        return '{0} {1}'.format(score_math,score_literatue)

n, m = map(int,input().split())
a = []
for i in range(n):
    temp = list(map(str,input().split()))
    a.append(temp)

b = []
for i in range(m):
    temp = str(input())
    b.append(temp)

c = []
d = []
for i in range(len(a)):
    std_code = a[i][0]
    math = a[i][1]
    literature = a[i][2]
    student = Student(std_code,math,literature)
    c.append(student)

for code in b:
    for i in range(len(a)):
        std_code = a[i][0]
        if code == std_code:
            x = i
            d.append(x)
            
for i in d:
    print(c[i].get_score())