class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        
        fast, i = head, 1
        while i <= n:
            fast = fast.next
            i += 1
        slow, prev = head, head
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            
        
        if slow == prev:
            return slow.next
    
        prev.next = slow.next
        
        
        return head