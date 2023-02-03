# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None
        
        if root.val == key:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            
            right_child = root.right
            
            right_most = root.left
            while right_most.right:
                right_most = right_most.right
            
            right_most.right = right_child
            return root.left
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        return root
            