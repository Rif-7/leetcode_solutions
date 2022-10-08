class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next_ = None, None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dct = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        
        self.left.next_, self.right.prev = self.right, self.left
        
    def remove(self, node):
        prev = node.prev
        next_ = node.next_
        
        prev.next_, next_.prev = next_, prev
    
    def updateRecent(self, node):
        prevRecent = self.right.prev
        prevRecent.next_, node.prev = node, prevRecent
        self.right.prev, node.next_ = node, self.right

    def get(self, key: int) -> int:
        node = self.dct.get(key)
        if node:
            self.remove(node)
            self.updateRecent(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if self.dct.get(key):
            node = self.dct[key]
            node.val = value
            self.remove(node)
            self.updateRecent(node)
            return
        
        elif self.capacity == self.size:
            lru = self.left.next_
            self.remove(lru)
            del self.dct[lru.key]
            self.size -= 1
        
        
        newNode = Node(key, value)
        self.updateRecent(newNode)
        self.dct[key] = newNode
        self.size += 1
        

