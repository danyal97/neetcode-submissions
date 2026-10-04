# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def rec(root, invert_tree):

            if root == None:
                return
            
            if root.left:
                invert_tree.right = TreeNode(root.left.val) 
                rec(root.left,invert_tree.right)

            if root.right:
                invert_tree.left = TreeNode(root.right.val) 
                rec(root.right,invert_tree.left)

        if root:
            invert_tree = TreeNode(root.val)
            rec(root,invert_tree)

            return invert_tree
        else:
            return None
        