class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        stack = [0]
        def findDepth(node):
            if not node:
                return 0
            leftDepth, rightDepth =  findDepth(node.left), findDepth(node.right)
            if leftDepth + rightDepth > stack[-1]:
                stack.append(leftDepth + rightDepth)
            return 1 + max(leftDepth, rightDepth)
        findDepth(root)
        return stack[-1]