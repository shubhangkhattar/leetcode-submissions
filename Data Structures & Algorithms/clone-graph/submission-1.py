"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        my_map = {}

        def dfs(node):
            
            if not node:
                return None
            
            new_node = Node(node.val)
            my_map[node] = new_node

            for neighbor in node.neighbors:
                if neighbor not in my_map:
                    new_node.neighbors.append(dfs(neighbor))
                else:
                    new_node.neighbors.append(my_map[neighbor])
                
            return new_node
            
        return dfs(node)