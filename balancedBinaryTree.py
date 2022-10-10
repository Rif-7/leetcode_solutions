class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def findDepth(node):
            if not node:
                return 1
            leftDepth, rightDepth = findDepth(node.left), findDepth(node.right)
            if not leftDepth or not rightDepth or abs(leftDepth - rightDepth) > 1:
                return False
            
            return 1 + max(leftDepth, rightDepth)
        
        return True if findDepth(root) else False