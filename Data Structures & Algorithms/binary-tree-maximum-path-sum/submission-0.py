# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.ans = float("-inf")

        def dfs(root):
            
            if not root:
                return 0

            sum_left = max(0,dfs(root.left)) # Not include the child
            
            sum_right = max(0,dfs(root.right))

            self.ans = max(self.ans,sum_right+sum_left+root.val)

            return max(sum_left,sum_right) + root.val

        dfs(root)
        
        return self.ans

    

