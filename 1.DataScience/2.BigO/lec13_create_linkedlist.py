class node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertTail(self,data):
        p = node(data,None)
        if self.head == None:
            self.head = self.tail = node(data,None)
        else:
            self.tail.next = p
            self.tail = p
            
    def print(self):
        itr = self.head
        while itr:
            print(itr.data, end = ' ')
            itr = itr.next
    
    def insert_value(self,a):
        for i in a:
            self.insertTail(i)

a = linkedlist()
b = linkedlist()

n = int(input())
c = input().split()
for i in range(len(c)):
    c[i] = int(c[i])

a.insert_value(c)
b.insertTail(a.head.data)

itr = a.head
while itr.next:
    b.insertTail(itr.data + itr.next.data)
    itr = itr.next
b.print()