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

        val = preorder[0]
        node = TreeNode(val)

        index = inorder.index(val)

        node.left = self.buildTree(preorder[1:index+1],inorder[:index+1])
        node.right = self.buildTree(preorder[1+index:],inorder[index+1:])

        return node
        

        # preorder = [1,2,3,4], inorder = [2,1,3,4]


        # (pre_q,in_q)
        

        # 1
        # 2, 2               3,4 | 3,4


