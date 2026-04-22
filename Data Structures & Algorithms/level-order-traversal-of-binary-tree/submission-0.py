# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            count = len(queue)
            inner_queue = []
            for i in range(count):
                
                node = queue.pop(0)
                inner_queue.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            ans.append(inner_queue)

        return ans
