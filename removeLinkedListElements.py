class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        node = head
        while node:
            if node.val ==  val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return dummy.next