# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        memo = {}
        
        def dfs(node,flag):
            
            if not node:
                return 0

            if (node,flag) in memo:
                return memo[(node,flag)]
            
            if flag: #True
                val = max(dfs(node.left,not flag) + dfs(node.right,not flag) + node.val, dfs(node.left,flag) + dfs(node.right,flag))
                
            else:
                val = dfs(node.left,not flag) + dfs(node.right,not flag)

            memo[node,flag] = val

            return val
            
        return dfs(root,True)
    