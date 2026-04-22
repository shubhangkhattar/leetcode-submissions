# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good_node_count = 0

        def countNode(node,maxVal):
            if not node:
                return
            
            nonlocal good_node_count 
            if node.val >= maxVal:
                good_node_count += 1
            
            maxVal = max(maxVal,node.val)
            
            countNode(node.left,maxVal)
            countNode(node.right,maxVal)
        
        countNode(root,float("-inf"))
        return good_node_count



            