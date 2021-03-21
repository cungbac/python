
def check_inverse(a):
    def inverse(n):
        if n == 0:
            return 0
        step = n // 10
        num = str(n % 10)
        func = str(inverse(step))
        return num + func
    if a == int(inverse(a))/10:
        return True
    else:
        return False

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


ll = linkedlist()

idx = 0
while True:
    n = int(input())
    if n == -1:
        break
    ll.insertTail(n)

ll_idx = linkedlist()
itr = ll.head
while itr:
    if check_inverse(itr.data):
        ll_idx.insertTail(idx)
    idx += 1
    itr = itr.next
ll_idx.print()
# m = 121
# print(check_inverse(m))