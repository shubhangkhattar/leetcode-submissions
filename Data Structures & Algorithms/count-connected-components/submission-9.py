class DSU:
    def __init__(self,n):
        self.par = list(range(n))
        self.rank = [1] * n

    def find(self,n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p1] = p2
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)
        for u,v in edges:
            if dsu.union(u,v):
                res -= 1
        return res
        


        

        