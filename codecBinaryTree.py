class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                return res.append("N")
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.i = -1
        data = data.split(",")
        def dfs():
            self.i += 1
            if data[self.i] == "N":
                return None
            node = TreeNode(int(data[self.i]))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()