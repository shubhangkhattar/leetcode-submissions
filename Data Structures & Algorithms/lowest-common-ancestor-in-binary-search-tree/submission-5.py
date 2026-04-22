# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not root:
            return root
        

        def helper(root):
            if p.val < root.val and q.val < root.val:
                return helper(root.left)
            elif p.val > root.val and q.val > root.val:
                return helper(root.right)
            else:
                return root
        
        return helper(root)