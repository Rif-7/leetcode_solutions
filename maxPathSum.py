class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MySolution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 
        res = float("-inf")
        def count(node):
            nonlocal res
            sum_, sum_left, sum_right = node.val, node.val, node.val
            if node.left:
                left = count(node.left)
                sum_left += left
                sum_ += left
            if node.right:
                right = count(node.right)
                sum_right += right
                sum_ += right
            res = max(res, sum_, sum_right, sum_left, node.val)
            return max(sum_right, sum_left, node.val)
        count(root)
        return res

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]
        