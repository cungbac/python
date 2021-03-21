import sys
sys.setrecursionlimit(100000)

class node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertTail(self,data):
        p = node(data)
        if self.head == None and self.tail == None:
            self.head = self.tail = p
        self.tail.next = p
        self.tail = p
    
    def insertHead(self,data):
        p = node(data)
        p.next = self.head
        self.head = p

    def insertHead_fibo(self):
        head = self.head
        next = self.head.next
        data = (head.data + next.data) % 1000007
        self.insertHead(data)

    def insert_list(self,lst):
        for data in lst:
            self.insertTail(data)
        

def inverse_list(a,n):
    if n == 0:
        return []
    else:
        return [a[n-1]] + inverse_list(a,n-1)
    

# Input & Output
a = linkedlist()

x, y, n = map(int,input().split())

m = [x,y]

# a.insert_list(m)

a.insertHead(x)
print(a.head.data, end = ' ')

a.insertHead(y)
print(a.head.data, end = ' ')

for i in range(n-2):
    a.insertHead_fibo()
    print(a.head.data, end = ' ')


