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
    
    def get_max_year(self):
        ans = self.head
        itr = self.head
        if self.head == None:
            return None
        while itr:
            if itr.data[2] > ans.data[2]:
                ans = itr
            itr = itr.next
        return ans.data[2]
    
    def get_max_month(self):
        ans = self.head
        itr = self.head
        if self.head == None:
            return None
        while itr:
            if itr.data[1] > ans.data[1]:
                ans = itr
            itr = itr.next
        return ans.data[1]

    def get_max_day(self):
        ans = self.head
        itr = self.head
        if self.head == None:
            return None
        while itr:
            if itr.data[0] > ans.data[0]:
                ans = itr
            itr = itr.next
        return ans.data[0]

    def print(self):
        itr = self.head
        while itr:
            print(itr.data[0],itr.data[1],itr.data[2], end = ' ')
            itr = itr.next

ll = linkedlist()
n = int(input())
for i in range(n):
    temp = list(map(int,input().split()))
    ll.insertTail(temp)

ll_max_year = linkedlist()
max_year = ll.get_max_year()

itr = ll.head
while itr:
    if itr.data[2] == max_year:
        ll_max_year.insertTail(itr.data)
    itr = itr.next

ll_max_month = linkedlist()
max_month = ll_max_year.get_max_month()
itr_year = ll_max_year.head
while itr_year:
    if itr_year.data[1] == max_month:
        ll_max_month.insertTail(itr_year.data)
    itr_year = itr_year.next

ll_max_day = linkedlist()
max_day = ll_max_month.get_max_day()
itr_month = ll_max_month.head
while itr_month:
    if itr_month.data[0] == max_day:
        ll_max_day.insertTail(itr_month.data)
    itr_month = itr_month.next

ll_max_day.print()