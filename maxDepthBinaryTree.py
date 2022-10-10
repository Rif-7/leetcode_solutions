class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def findDepth(node):
            if not node:
                return 0
            return 1 + max(findDepth(node.left), findDepth(node.right))
        return findDepth(root)