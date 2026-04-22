# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        globalDepth = 0

        def calcDepth(root,depth):
            
            if not root:
                return

            nonlocal globalDepth

            depth += 1

            globalDepth = max(depth,globalDepth)

            calcDepth(root.left,depth)
            calcDepth(root.right,depth)
        
        calcDepth(root,0)
        
        return globalDepth