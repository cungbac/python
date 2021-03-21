class Student:
    def __init__(self,score_math = 0, score_literature = 0):
        # self.name = name
        self.score_math = score_math
        self.score_literature = score_literature
    
    def avg_score(self):
        avg_score = (self.score_math + self.score_literature)/2
        return avg_score


n = int(input())
a = []
for i in range(n*2):
    temp = input()
    a.append(temp)

b = []
for i in range(1,len(a),2):
    b.append(a[i])

count = 0
for i in range(len(b)):
    score_math = float(b[i][:b[i].find(' ')])
    score_literature = float(b[i][b[i].find(' ')+1:])
    student = Student(score_math,score_literature)
    if student.avg_score() >= 9:
        count += 1
print(count)