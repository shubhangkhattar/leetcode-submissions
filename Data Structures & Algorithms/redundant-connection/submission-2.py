class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        pa = [i for i in range(n + 1)]
        
        def find(node):
            if pa[node] != node:
                return find(pa[node])  # Recursive find, no path compression
            return node
        
        def union(node_1, node_2):
            p1, p2 = find(node_1), find(node_2)
            if p1 == p2:
                return True  # Already in the same set (redundant)
            pa[p1] = p2  # Union the two sets
            return False
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
