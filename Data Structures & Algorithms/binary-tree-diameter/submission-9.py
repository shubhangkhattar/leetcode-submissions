# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDia = 0

        def calcDia(root):

            if not root:
                return 0

            nonlocal maxDia

            leftSum = calcDia(root.left)
            rightSum = calcDia(root.right)

            maxDia = max(leftSum + rightSum, maxDia)

            return max(leftSum,rightSum) + 1

        calcDia(root)
        return maxDia
        