class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        pa = [i for i in range(n+1)]

        def find(node):
            if node == pa[node]:
                return node
            return find(pa[node])

        def union(node_1, node_2):
            p1,p2 = find(node_1), find(node_2)
            if p1 == p2:
                return True
            
            pa[p1] = p2
        
        for u,v in edges:
            if union(u,v):
                return [u,v]
