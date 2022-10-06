
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        

class MySolution:
    def copyRandomList(self, head):
        prevMap = {}
        tail = head
        def makeCopy(t):
            if not t:
                return None
            curr = Node(t.val)
            curr.next = makeCopy(t.next)
            prevMap[t] = curr
            return curr
        head2 = makeCopy(tail)
        tail1, tail2 = head, head2
        while tail1:
            if tail1.random:
                tail2.random = prevMap[tail1.random]
            tail1 = tail1.next
            tail2 = tail2.next

        return head2

class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]