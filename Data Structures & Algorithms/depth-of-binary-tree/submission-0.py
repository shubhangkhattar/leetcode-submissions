# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        if not root:
            return 0

        def depth_calc(root,depth):
            self.max_depth = max(self.max_depth,depth)
            
            if root.left:
                depth_calc(root.left,depth+1)

            if root.right:
                depth_calc(root.right,depth+1)

        depth_calc(root,1)
        return self.max_depth