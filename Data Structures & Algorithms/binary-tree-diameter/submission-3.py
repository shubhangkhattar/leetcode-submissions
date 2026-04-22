class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)

        diameter = left_height + right_height

        return max(diameter,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))



    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))