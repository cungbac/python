class student:
    def __init__(self,code,score):
        self.std_code = code
        self.std_score = score

    def update_code(self,newcode):
        self.std_code = newcode
    
    @ classmethod
    def from_list(cls,lst):
        lst[1] = float(lst[1])
        std_code, std_score = lst
        return cls(std_code,std_score)


def insertionSort_Asc(a):
    if len(a) == 1:
        return a
    lst_score = [a[0].std_score]
    lst_code = [a[0].std_code]
    for j in range(1,len(a)):
        lst_score.append(a[j].std_score)
        lst_code.append(a[j].std_code)
        key_score = a[j].std_score
        key_code = a[j].std_code
        exchange = a[j]
        i = j
        while i >= 0:
            if i == 0:
                break
            if lst_score[i-1] > key_score:
                break
            if lst_score[i-1] == key_score and lst_code[i-1] < key_code:
                break
            lst_score[i] = lst_score[i-1]
            a[i] = a[i-1]
            i -= 1
        lst_score[i] = key_score
        a[i] = exchange
    return a

n, m = map(int,input().split())
a = []
for i in range(n):
    a.append(student.from_list(list(input().split())))

b = insertionSort_Asc(a)

for i in range(m):
    print(b[i].std_code)

