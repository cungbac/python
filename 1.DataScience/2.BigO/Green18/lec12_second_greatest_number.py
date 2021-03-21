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
            print(itr.data, end = ' ')
            itr = itr.next
    
    def max(self):
        itr = self.head
        ans = self.head
        if self.head == None:
            return None
        while itr:
            if itr.data > ans.data:
                ans = itr
            itr = itr.next
        return ans.data

    def remove_max(self):
        itr = self.head
        pre = node(None,itr)
        max = self.max()
        while itr:
            if itr.data == max:
                if itr.next == None:
                    pre.next = None
                    itr = pre.next
                    break
                else:
                    pre.next = itr.next
                    itr = itr.next
            pre = itr
            itr = itr.next

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def count_max(self):
        max = self.max()
        itr = self.head
        count = 0
        while itr:
            if itr.data == max:
                count += 1
            itr = itr.next
        return count

ll = linkedlist()
while True:
    n = float(input())
    if n == -1:
        break
    else:
        ll.insertTail(n)
        
        
ll.remove_max()
# print(ll.count_max())
if ll.length() == 1:
    print(-1)
elif ll.length() == ll.count_max():
    print(-1)
else:
    print(ll.max())
# ll.print()