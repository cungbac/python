import sys
sys.setrecursionlimit(500000)
class node:
    def __init__(self, x = 0, left = None, right = None):
        self.data = x
        self.left = left
        self.right = right

    def addToNode(self,x):
        cur = self.data
        if x < self.data:
            if self.left == None:
                p = node(x)
                self.left = p
            else:
                self.left.addToNode(x)
        elif x > self.data:
            if self.right == None:
                p = node(x)
                self.right = p
            else:
                self.right.addToNode(x)
        else:
            return

class BST:
    def __init__(self):
        self.root = None

    def addToBST(self,data):
        p = node(data)
        if self.root == None:
            self.root = p
        else:
            self.root.addToNode(data)
    
    def minBST(self):
        cur = self.root
        ans = self.root
        while cur.left:
            if cur.left.data < ans.data:
                ans.data = cur.left.data
                cur = cur.left
        return ans.data

a = BST()
n = int(input())
temp = input().split()
for i in range(len(temp)):
    a.addToBST(int(temp[i]))
    
print(a.minBST())