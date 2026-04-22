# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        def inorder(node,result):

            if not node:
                return 
            
            inorder(node.left,result)
            result.append(node.val)
            inorder(node.right,result)

            return result
        
        result = []

        inorder(root,result)

        return result
