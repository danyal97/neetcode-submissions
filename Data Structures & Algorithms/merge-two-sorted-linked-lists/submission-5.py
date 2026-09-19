# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        p = None
        d = None
        while list1!=None and list2!=None:

            if list1.val < list2.val:
                if p == None:
                    p = ListNode(list1.val)
                    d = p 
                else:
                    p.next = ListNode(list1.val)
                    p = p.next
                list1 = list1.next
            
            elif list2.val < list1.val:
                if p == None:
                    p = ListNode(list2.val)
                    d = p
                else:
                    p.next = ListNode(list2.val)
                    p = p.next
                list2 = list2.next
            else:
                if p == None:
                    p = ListNode(list2.val)
                    d = p
                    p.next = ListNode(list1.val)
                    p = p.next
                else:
                    p.next = ListNode(list2.val)
                    p = p.next
                    p.next = ListNode(list1.val)
                    p = p.next
                list2 = list2.next
                list1 = list1.next

        while list1 != None:
            if p == None:
                p = ListNode(list1.val)
                d =p
            else:
                p.next = ListNode(list1.val)
                p = p.next
            list1 = list1.next
        
        while list2 != None:
            if p == None:
                p = ListNode(list2.val)
                d =p
            else:
                p.next = ListNode(list2.val)
                p = p.next
            list2 = list2.next       
        
        # if d 
        return d            
                
                


        