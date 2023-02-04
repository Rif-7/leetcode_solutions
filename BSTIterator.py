# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root):
        self.iterator = []
        self.i = 0
        self.makeInorder(root)
        

    def next(self) -> int:
        val = self.iterator[self.i]
        self.i += 1
        return val

    def hasNext(self) -> bool:
        return self.i < len(self.iterator)
    
    def makeInorder(self, node):
        if not node:
            return 
        self.makeInorder(node.left)
        self.iterator.append(node.val)
        self.makeInorder(node.right)
        
