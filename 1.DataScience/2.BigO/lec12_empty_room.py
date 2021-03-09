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
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    
    def print(self):
        itr = self.head
        while itr:
            print(itr.data[0], itr.data[1])
            itr = itr.next

n = int(input())
ll = linkedlist()
for i in range(n):
    temp = input().split()
    ll.insertTail(temp)

ll_empty = linkedlist()
itr = ll.head
while itr:
    if itr.data[2] == '0':
        ll_empty.insertTail(itr.data)
    itr = itr.next

ll_empty.print()

