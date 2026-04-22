# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        result = []

        if not root:
            return result

        queue.append(root)

        while queue:
            level_right_element = None
            level_n = len(queue)
            for i in range(level_n):
                element = queue.pop(0)
                level_right_element = element.val
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            
            result.append(level_right_element)
        
        return result