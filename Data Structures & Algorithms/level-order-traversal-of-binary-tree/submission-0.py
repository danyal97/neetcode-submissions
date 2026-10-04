# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        q = [root]
        ans = []
        while len(q) != 0:
            
            new_array = []
            for i in q:
                if i.right:
                    new_array.append(i.right)
                if i.left:
                    new_array.append(i.left)
                


            arr = []

            while len(q):
                arr.append(q.pop().val)
            ans.append(arr)
            q = new_array
            
        return ans
        # print(arr)
            
        
        