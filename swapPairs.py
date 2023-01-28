# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        
        prev, next = dummy, None
        first, second = head, head.next
        
        while second:
            next = second.next
            prev.next = second
            second.next = first
            first.next = next
            
            prev = first
            
            first = next
            second = first.next if first else None
        
        return dummy.next