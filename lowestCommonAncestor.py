class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MySolution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        left, right, ancestor = root, root, root
        while left and right:
            if p.val < left.val:
                left = left.left
            elif p.val > left.val:
                left = left.right
            
            if q.val < right.val:
                right = right.left
            elif q.val > right.val:
                right = right.right
            
            if left == right:
                ancestor = left
                
            if left.val == p.val and right.val == q.val:
                return ancestor

class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
            