# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root, val: int):
        if not root:
            return TreeNode(val)
        
        node = root
        while node:
            if val > node.val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            if val < node.val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
        
        return root
        
            