class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        def connect(i, j):
            if j < i:
                return None
            
            mid = (i + j) // 2
            node = TreeNode(nums[mid])
            
            node.left = connect(i, mid - 1)
            node.right = connect(mid + 1, j)
            
            return node
        
        return connect(0, len(nums) - 1)
            
            