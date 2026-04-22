# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        cache = {}
        
        def dfs(node,choriPossible):
            nonlocal cache
            if not node:
                return 0

            if (node,choriPossible) in cache:
                return cache[(node,choriPossible)]
                
            chori_paise = 0
            if choriPossible:
                chori_paise = dfs(node.left,False) + dfs(node.right,False) + node.val

            no_chori = dfs(node.left,True) + dfs(node.right,True)

            cache[(node,choriPossible)] = max(chori_paise,no_chori)

            return cache[(node,choriPossible)]
        
        return dfs(root,True)