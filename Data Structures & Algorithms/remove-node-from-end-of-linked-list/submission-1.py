# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        l = 0
        h = head
        while h!=None:
            h = h.next
            l+=1

        nv = l-n

        l = 0
        prev = None
        h = head
        while h !=None:
            if l == nv:
                if prev == None:
                    head = head.next
                    h = head
                else:
                    prev.next = h.next
                    h = None
                    h = prev
            prev = h
            if h:
                h = h.next
            else:
                break
            l+=1
        
        return head
        