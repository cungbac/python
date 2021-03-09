# Class
class Fraction:
    def __init__(self, a = 1, b = 1):
        self.numerator = a
        self.denominator = b
    
    def gdc(self,a,b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def reduceFraction(self):
        if self.numerator == 0:
            self.denominator = 1
        x = self.gdc(abs(self.numerator),abs(self.denominator))
        self.numerator = int(self.numerator / x)
        self.denominator = int(self.denominator / x)
        return self

    def division(self):
        div = self.numerator / self.denominator
        return div
    
    def __str__(self):
        s = '{0} {1}'.format(self.numerator,self.denominator)
        return s

# Function  

def get_idx_max(a):
    max = 0
    for i in range(len(a)):
        num = a[i][0]
        denom = a[i][1]
        fract = Fraction(num,denom)
        div = fract.division()
        if div >= max:
            max = div
            x = i
    return x

# Input and Output    
n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

idx = get_idx_max(a)

fraction = Fraction(a[idx][0],a[idx][1])
fraction.reduceFraction()

print(fraction)

