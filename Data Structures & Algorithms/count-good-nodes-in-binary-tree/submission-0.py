# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,upper_bound):
            if not root:
                return 0
            
            count = 0
            if root.val >= upper_bound:
                count += 1
                upper_bound = root.val

            return count + dfs(root.left,upper_bound) + dfs(root.right,upper_bound) 

        return dfs(root, root.val)
            
