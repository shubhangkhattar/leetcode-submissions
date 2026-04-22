# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalanced = True

        def helper(root):

            nonlocal isBalanced

            
            if not root:
                return 0
            
            left_count = helper(root.left) 
            right_count = helper(root.right)

            if abs(right_count - left_count) > 1:
                isBalanced = False
            
            return max(left_count,right_count) + 1
        
        helper(root)

        return isBalanced