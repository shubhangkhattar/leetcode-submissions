# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        

        def dfs(root):
            if root is None:
                return "N"
            
            return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

        
        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = deque(data.split(","))  # Use a queue for easy traversal
        
        def dfs():
            if values:
                val = values.popleft()
                if val == "N":
                    return None
                
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
                return node
        
        return dfs()
