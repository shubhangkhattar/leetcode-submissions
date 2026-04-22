class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = list(range(n+1))
        rank = [0] * (n+1)

        def find(p):
            if p != par[p]:
                par[p] = find(par[p])
            return par[p]

        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p2] += rank[p1]
            else:
                par[p1] = p2
                rank[p1] += rank[p2]
            
            return True

        for u,v in edges:
            if not union(u,v):
                return [u,v]
            
            