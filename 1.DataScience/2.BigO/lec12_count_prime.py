def isPrime(n):
        if n == 1:
            return False
        if n <= 2:
            return True
        for i in range(2,n):
            if n % i == 0:
                return False
        return True

class node:
    def __init__(self, data = None, next = None):
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
            self.head = self.tail = node(data,None)
        else:
            self.tail.next = p
            self.tail = p

    def count_prime(self):
        count = 0
        itr = self.head
        while itr:
            if isPrime(itr.data):
                count += 1
            itr = itr.next
        return count


a = linkedlist()
while True:
    data = int(input())
    if data == -1:
        break
    a.insertTail(data)

print(a.count_prime())