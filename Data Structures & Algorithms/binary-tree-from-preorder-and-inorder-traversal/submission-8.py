# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None

        nodeVal = preorder[0]
        countLeft = inorder.index(nodeVal)

        node = TreeNode(nodeVal)

        node.left = self.buildTree(preorder[1:countLeft+1],inorder[:countLeft])
        node.right = self.buildTree(preorder[countLeft+1:],inorder[countLeft+1:])

        return node


# 0,5,4,3,2,1,0

# 0,1,2,3,4,5,6

# index = 3
# val = 3

