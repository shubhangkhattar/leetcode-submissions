# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global isBalanced
        isBalanced = True

        def dfs(root):
            global isBalanced

            if isBalanced == False:
                return 0
            
            if root is None:
                return 0
            
            left_height = 1 + dfs(root.left)
            right_height = 1 +  dfs(root.right)

            if abs(left_height - right_height) > 1:
                isBalanced = False
                return 0
            
            return max(left_height,right_height)

        dfs(root) 

        return isBalanced

