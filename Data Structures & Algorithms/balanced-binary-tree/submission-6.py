# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        checkHeight = True

        def check(root):

            nonlocal checkHeight

            if not root:
                return 0

            left_height = check(root.left) 
            right_height = check(root.right)

            if abs(right_height - left_height) > 1:
                checkHeight = False

            return max(left_height,right_height) + 1
        
        check(root)
        return checkHeight