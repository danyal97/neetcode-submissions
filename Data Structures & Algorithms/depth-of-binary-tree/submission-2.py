# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def rec(root,count,ans):

            if root == None:
                return max(ans,count)
            
            count+=1
            ans = rec(root.left,count,ans)
            ans = rec(root.right,count,ans)

            return ans
        
        return(rec(root,0,0))
        

        