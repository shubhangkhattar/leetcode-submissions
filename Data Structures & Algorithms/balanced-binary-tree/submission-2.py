# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        isBalanced = True

        def dfs(root):
            nonlocal isBalanced
            if not root:
                return 0
            
            right = dfs(root.right)
            left = dfs(root.left)

            if abs(right - left) > 1:
                isBalanced = False

            return max(right,left) + 1 

        dfs(root)
        return isBalanced
    

