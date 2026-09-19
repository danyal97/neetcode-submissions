# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # n = head
        fast = head
        while head !=None:
            if fast.next == None:
                return False
            fast = fast.next.next
            if fast == None:
                return False
            if fast == head:
                return True
            head = head.next
        
        return False
        