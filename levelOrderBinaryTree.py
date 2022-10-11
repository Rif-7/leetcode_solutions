from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        res = []
        que = deque()
        que.append(root)
        while que:
            val = []
            for i in range(len(que)):
                curr = que.popleft()
                val.append(curr.val)
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
            res.append(val)
        return res