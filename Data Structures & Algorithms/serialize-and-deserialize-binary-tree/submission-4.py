# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.encoding = []

        def dfs(node):
            if not node:
                self.encoding.append("N")
                return
            
            self.encoding.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(self.encoding)


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        self.encoding = data.split(",")
        self.i = 0

        def dfs():
            if self.encoding[self.i] == "N":
                return None
            
            node = TreeNode(self.encoding[self.i])
            self.i += 1
            node.left = dfs()
            self.i += 1
            node.right = dfs()

            return node
        
        return dfs()

