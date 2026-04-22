# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return False

        globalAns = False

        def isSameTree(p, q):

            if not p and not q:
                return True
            
            if not p or not q:
                return False

            return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        

        def check(root):
            if not root:
                return
            
            
            nonlocal globalAns
            
            if not globalAns and root.val == subRoot.val:
                globalAns = isSameTree(root,subRoot)

            check(root.left)
            check(root.right)

        check(root)
        return globalAns        
        
            
            