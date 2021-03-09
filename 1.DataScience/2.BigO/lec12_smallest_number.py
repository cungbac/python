class Node:
    def __init__(self,x=None):
        self.data = x
        self.next = None

class LinkedList:
    def __init__(self):
        # a = [] (empty array)
        self.head = None
        self.tail = None

    def insertTail(self,x):
        p = Node(x)
        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
        
    def insertHead(self,x):
        p = Node(x)
        if self.head == None:
            self.head = self.tail = p
        else:
            cur = self.head
            self.head = p
            self.head.next = cur
    
    def min_linked(self):
        ans = self.head
        cur = self.head # current
        while cur != None:
            if cur.data < ans.data:
                ans = cur
            cur = cur.next
        return ans

a = LinkedList()
b = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        a.insertHead(n)

print(a.min_linked().data)