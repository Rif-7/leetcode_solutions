class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return False
            
            if self.checkIfEqual(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
            
        
    def checkIfEqual(self, t1, t2):
        def dfs(node1, node2):
            if not node1 or not node2:
                return node1 == node2
            elif node1.val != node2.val:
                return False
            else:
                return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
        return dfs(t1, t2)