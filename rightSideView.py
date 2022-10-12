from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MySolution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []
        level, curL = 0, 0
        res = []
        def dfs(node, currLevel):
            nonlocal level
            if currLevel > level:
                res.append(node.val)
                level += 1
                
            if node.right:
                dfs(node.right, currLevel + 1)
            if node.left:
                dfs(node.left, currLevel + 1)
                
        dfs(root, 1)
        
        return res

class Solution:
    def rightSideView(self, root: TreeNode):
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res