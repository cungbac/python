class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
    
    def insertHead(self,data):
        a = node(data,self.head)
        self.head = a
    
    def insertTail(self,data):
        if self.head == None:
            self.head = node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = node(data,None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr != None:
            count += 1
            itr = itr.next
        return count

    def get_sum(self):
        sum_link = 0
        itr = self.head
        while itr:
            sum_link = sum_link + itr.data
            itr = itr.next
        return sum_link

a = linkedlist()
while True:
    x = float(input())
    if x == -1:
        break
    a.insertTail(x)

itr = a.head
while itr:
    if itr.data < 5:
        print(itr.data)
    itr = itr.next