class node:
    def __init__(self, data = 0):
        self.data = data
        self.left = None
        self.right = None
    
    def addToNode(self,data):
        cur = self.data
        left = self.left
        right = self.right
        if data < self.data:
            if self.left == None:
                p = node(data)
                self.left = p
            else:
                self.left.addToNode(data)
        if data > self.data:
            if self.right == None:
                p = node(data)
                self.right = p
            else:
                self.right.addToNode(data)
        else:
            return

    def getInOrder(self):
        lst = []
        cur = self.data
        left = self.left
        right = self.right
        if self.left != None:
            lst += self.left.getInOrder()
        
        lst.append(self.data)

        if self.right != None:
            lst += self.right.getInOrder()
        
        return lst
      
def build_tree(lst):
    root = node(lst[0])

    for i in range(1,len(lst)):
        root.addToNode(lst[i])
    
    return root


n = int(input())
a = input().split()
for i in range(n):
    a[i] = int(a[i])

tree = build_tree(a)
lst = tree.getInOrder()
for i in range(len(lst)):
    print(lst[i],end = ' ')