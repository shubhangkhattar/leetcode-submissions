# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0

        if not root:
            return count

        q = deque([(root,float("-inf"))])
        while q:
            node,pre_max = q.popleft()
            if node.val >= pre_max:
                count += 1
            pre_max = max(pre_max,node.val)
            if node.left:
                q.append((node.left,pre_max))
            if node.right:
                q.append((node.right,pre_max))

        return count
            

        

            




        