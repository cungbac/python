def is_five_divisor(n):
    if n % 5 == 0 and n % 10 != 0:
        return True
    return False

class node:
    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertHead(self,data):
        p = node(data,self.head)
        self.head = p
    
    def insertTail(self,data):
        p = node(data,None)
        if self.head == None:
            self.head = self.tail = p
        else:
            self.tail.next = p
            self.tail = p
    
    def remove_5_at_last(self):
        cur = self.head
        tail = self.tail
        pre = node(None,cur)

        if is_five_divisor(self.head.data):
            self.head = self.head.next
            pre = node(None,self.head)
        
        while cur:
            if cur.next == None:
                break
            if is_five_divisor(self.head.data):
                self.head = self.head.next
                pre = node(None,cur)
            if is_five_divisor(cur.data):
                pre.next = cur.next
                cur = pre.next
            cur = cur.next
            pre = pre.next

    def removeTail(self):
        if self.head == None:
            return None
        if self.head.next == None:
            head = None
            return None
        itr = self.head
        while itr.next.next:
            itr = itr.next
        if is_five_divisor(itr.next.data):
            itr.next = None
        return itr

a = linkedlist()
n = int(input())

for i in range(n):
    data = int(input())
    if is_five_divisor(data) == False:
        a.insertTail(data)

# a.remove_5_at_last()
# a.removeTail()

itr = a.head
while itr:
    print(itr.data, end = ' ')
    itr = itr.next

# print(a.tail.data)