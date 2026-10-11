# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def rec(node, low, high):
            if node == None:
                return True
            
            if not (low < node.val < high):
                return False

            return rec(node.right, node.val, high) and rec(node.left, low, node.val)
        
            

        return(rec(root, -float('inf'), float('inf') ))  
        