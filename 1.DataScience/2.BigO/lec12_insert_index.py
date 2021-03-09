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
      return
    self.tail.next = p
    self.tail = p
  def printList(self):
    cur = self.head
    while cur:
      print(cur.data, end = ' ')
      cur = cur.next

num = 1
l = linkedlist()
while True:
  n = int(input())
  if n == 0:
    break
  l.insertTail(num)
  l.insertTail(n)
  num += 1

l.printList()
  