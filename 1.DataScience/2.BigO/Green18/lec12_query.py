class node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertTail(self,data):
        p = node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    
    def removeHead(self):
        if self.head == None:
            return None
        self.head = self.head.next

    def print(self):
        itr = self.head
        while itr:
            print(itr.data, end = ' ')
            itr = itr.next

n = int(input())
a = []
for i in range(n):
    temp = list(map(int,input().split()))
    a.append(temp)

ll = linkedlist()
for i in range(len(a)):
    if len(a[i]) == 2:
        ll.insertTail(a[i][1])
    else:
        ll.removeHead()
ll.print()

