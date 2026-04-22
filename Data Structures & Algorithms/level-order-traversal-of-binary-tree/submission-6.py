# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = collections.deque()
        queue.append(root)
        result = []

        if not root:
            return result

        while queue:
            inner_list = []
            element_count = len(queue)
            for i in range(element_count):
                node = queue.popleft()
                inner_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(inner_list)

        return result
