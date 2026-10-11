# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []
        def rec(node):
            if node == None:
                return
            
            # print(a)
            rec(node.left)
            a.append(node.val)
            rec(node.right)

        rec(root)
        # a.sort()
        return a[k-1]
        