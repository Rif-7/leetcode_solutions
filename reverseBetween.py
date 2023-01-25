class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        
        right = right - left
        dummy = ListNode()
        dummy.next = head
        
        l_node, l_prev = head, dummy
        while (left > 1):
            left -= 1
            l_prev = l_node
            l_node = l_node.next
            
        r_node = l_node
        while (right > 0):
            right -= 1
            r_node = r_node.next
        r_next = r_node.next
        
        prev, curr = None, l_node
        while curr != r_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        l_node.next = r_next
        l_prev.next = r_node
        
        return dummy.next
        
        
            
            