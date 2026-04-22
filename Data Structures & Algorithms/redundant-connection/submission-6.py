class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        adj = [[] for _ in range(n+1)]
        pa = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(node):
            if node != pa[node]:
                pa[node] = find(pa[node])
            return pa[node]

        def union(node_1, node_2):
            p1,p2 = find(node_1), find(node_2)
            if p1 == p2:
                return True
            
            if rank[p1] >= rank[p2]:
                pa[p2] = p1
                rank[p1] += rank[p2]
            else:
                pa[p1] = p2
                rank[p2] += rank[p1]
            return False
        
        for u,v in edges:
            if union(u,v):
                return [u,v]
