# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")


        def dfs(root):

            if not root:
                return 0
            
            nonlocal maxSum

            leftSum = dfs(root.left)
            rightSum = dfs(root.right)

            maxSum = max(maxSum, leftSum+root.val,rightSum+root.val,root.val,rightSum+ leftSum+root.val )

            return max(leftSum+root.val,rightSum+root.val,root.val)

        
        dfs(root)

        return maxSum