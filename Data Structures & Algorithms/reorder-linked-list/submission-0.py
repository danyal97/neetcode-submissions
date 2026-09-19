# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        start = head
        ll = []

        while start!= None:
            ll.append(start)
            start = start.next
        
        n = len(ll)
        i = 0
        j = 0
        head = ListNode(0, None)
        while i < math.ceil(n /2 ):
            ll[i].next = None
            ll[n-i-1].next = None
            
            
            
            head.next = ll[i]
            if ll[i] == ll[n-i-1]:
                break
            head = head.next
            head.next = ll[n-i-1]
            
            head = head.next
            i+=1
        