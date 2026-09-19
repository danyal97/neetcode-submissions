# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        p = None
        while head != None:
            tmp = head.next
            head.next = p
            p = head
            head = tmp
        
        # ans = []
        
        # while p != None:
        #     ans.append(p)
        #     p = p.next

        # print(ans)
        return p
        # p

        