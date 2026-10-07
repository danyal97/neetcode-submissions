# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def rec(node, node_2):

            if node == None and node_2 != None: return False

            if node != None and node_2 == None: return False

            if node != None and node_2 != None:
                if node.val != node_2.val: return False

                if node.val == node_2.val: 
                    if rec(node.right, node_2.right) == False:
                        return False
                    if rec(node.left, node_2.left) == False:
                        return False
                    
            return True
        
        return(rec(p,q))