class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:

    def __init__(self):
        self.head = TreeNode()

    def insert(self, word: str) -> None:
        if not word:
            return
        prev = self.head
        for c in word:
            if prev.children.get(c):
                prev = prev.children[c]
                continue
            node = TreeNode()
            prev.children[c] = node
            prev = node
        prev.end = True
            

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if not curr.children.get(c):
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if not curr.children.get(c):
                return False
            curr = curr.children[c]
        return True
