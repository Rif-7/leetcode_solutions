class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def invert(node):
            if not node:
                return 0
            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)
        invert(root)
        return root