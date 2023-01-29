# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1, root2):
        def merge(node1, node2):
            if not node1 and not node2:
                return None
            
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            node = TreeNode(val1 + val2)
            
            # Node 1's left and right childs
            left1 = node1.left if node1 else None
            right1 = node1.right if node1 else None
            
            # Node 2's left and right childs
            left2 = node2.left if node2 else None
            right2 = node2.right if node2 else None
            
            node.left = merge(left1, left2)
            node.right = merge(right1, right2)
            
            return node
        
        return merge(root1, root2)
            