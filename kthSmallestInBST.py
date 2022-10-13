class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MySolution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        i = 0
        val = None
        def inorder(node):
            nonlocal i
            nonlocal val
            if not node:
                return False
            
            inorder(node.left)
            i += 1
            if i == k:
                val = node.val
                return
            inorder(node.right)
        inorder(root)
        return val