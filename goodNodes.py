class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return []
        
        res = 0
        def dfs(node, maxVal):
            if not node:
                return
            nonlocal res
            if maxVal <= node.val:
                maxVal = node.val
                res += 1
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root, root.val)
        return res