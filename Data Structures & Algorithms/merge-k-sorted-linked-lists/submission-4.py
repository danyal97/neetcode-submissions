# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        def mergeTwolist(l1,l2):

            head = None
            tmp  = None
            
            while l1 !=None and l2!=None:
                if l1.val == l2.val:
                    if head == None:
                        head = ListNode(l1.val, None)
                        tmp = head

                        tmp.next = ListNode(l2.val, None)
                        tmp = tmp.next

                    else:
                        tmp.next = ListNode(l1.val, None)
                        tmp = tmp.next
                        tmp.next = ListNode(l2.val, None)
                        tmp = tmp.next
                    
                    l1 = l1.next
                    l2 = l2.next

                else:
                    mn_value = l1.val

                    if l1.val < l2.val:
                        mn_value = min(mn_value ,l1.val)
                        l1 = l1.next

                    elif l2.val < l1.val:
                        mn_value = min(mn_value ,l2.val)
                        l2 = l2.next

                    if head == None:
                        head = ListNode(mn_value, None)
                        tmp = head
                    else:
                        tmp.next = ListNode(mn_value, None)
                        tmp = tmp.next

            while l2!=None:
                if head == None:
                    head = ListNode(l2.val, None)
                    tmp = head
                else:
                    tmp.next = ListNode(l2.val, None)
                    tmp = tmp.next
                l2 = l2.next

            while l1!=None:
                if head == None:
                    head = ListNode(l1.val, None)
                    tmp = head
                else:
                    tmp.next = ListNode(l1.val, None)
                    tmp = tmp.next
                l1 = l1.next
            
            return head

        if len(lists) == 0:
            return None
        while len(lists)!=1:
            ml = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = None
                if i+1 < len(lists): 
                    l2 = lists[i+1]
                ml.append(mergeTwolist(l1,l2))
            lists = ml
        # print(ml)

        return lists[0]
        