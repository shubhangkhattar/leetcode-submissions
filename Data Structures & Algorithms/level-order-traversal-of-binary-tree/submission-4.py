from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)

        if not root:
            return []

        def helper(node,depth):

            result[depth].append(node.val)

            if node.left:
                helper(node.left,depth+1)
            
            if node.right:
                helper(node.right,depth+1)
        
        helper(root,0)

        final_result = []

        for key in sorted(result):
            final_result.append(result[key])
        
        return final_result
            

            
            

        
