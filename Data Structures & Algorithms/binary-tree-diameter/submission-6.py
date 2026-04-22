# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        def dfs(root):
            if not root:
                return 0
            
            left_sub = dfs(root.left)
            right_sub = dfs(root.right)
            
            self.max_dia = max(left_sub + right_sub,self.max_dia)

            return 1 + max(left_sub,right_sub)

        dfs(root)
        return self.max_dia
