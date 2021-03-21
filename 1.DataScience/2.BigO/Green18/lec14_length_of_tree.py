class node:
    def __init__(self, data = 0):
        self.data = data
        self.left = None
        self.right = None
    
    def addToNode(self,data):
        cur = self.data
        left = self.left
        right = self.right

        p = node(data)

        if data < self.data:
            if left == None:
                left = p
            else:
                left.addToNode(data)
        if data > self.data:
            if right == None:
                right = p
            else:
                right.addToNode(data)
        else:
            return

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def addToBST(self,data):
        p = node(data)
        if self.root == None:
            self.root = p
        else:
            self.root.addToNode(data)

    def print_tree(self):
        cur = self.root
        print(cur.data)
        while cur.left:
            print(cur.left.data)
        while cur.right:
            print(cur.right.data)

a = [i for i in range(10)]

# print(a)

tree = BinaryTree()

a = [6,4,7,9,10,2,3,6]
for i in a:
    tree.addToBST(i)

tree.print_tree()