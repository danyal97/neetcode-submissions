# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        q = [subRoot]
        c = 0
        while len(q):
            n = q.pop()
            c+=1
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        # print(c)
        # count = 0
        def dfs(n1,n2):
            if n1 == None and n2 == None:
                return 1
            if n1 == None or n2 == None:
                return 0
            if n1.val == n2.val:
                return dfs(n1.left,n2.left) + dfs(n1.right, n2.right)
            return 0

        q = [root]

        while len(q):
            node = q.pop()
            count = 0
            # print(dfs(node, subRoot))
            if node.val == subRoot.val and dfs(node, subRoot) == c+1:
                return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
                
        