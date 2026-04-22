# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        def helper(root,max_val):

            nonlocal count

            if not root:
                return
            if root.val >= max_val:
                count += 1
            
            helper(root.left,max(max_val,root.val))
            helper(root.right,max(max_val,root.val))

        helper(root,float("-inf"))

        return count

