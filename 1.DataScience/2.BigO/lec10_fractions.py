class Fraction:
    def __init__(self,a=1,b=100):
        self.num = a
        self.denom = b
    
    def glc(self,a,b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def sumFraction(self,p2):
        p3 = Fraction()
        p3.num = self.num*p2.denom + self.denom*p2.num
        p3.denom = self.denom * p2.denom
        return p3

    def reduceFraction(self):
        if self.num == 0:
            self.denom = 1
        x = self.glc(abs(self.num),abs(self.denom))
        self.num = self.num // x
        self.denom = self.denom // x
        return self
    
    def __str__(self):
        s = '{0} {1}'.format(self.num,self.denom)
        return s

a, b = map(int,input().split())
p1 = Fraction(a,b)

c, d = map(int,input().split())
p2 = Fraction(c,d)

p3 = p1.sumFraction(p2)
p3.reduceFraction()
print(p3)

