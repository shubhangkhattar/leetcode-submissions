class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)

        def dfs(node,prev):
            
            nonlocal visited

            if visited[node]:
                return True
            
            visited[node] = True

            for neigh in adj[node]:
                if neigh == prev:
                    continue
                if dfs(neigh,node):
                    return True
            
            return False

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
            visited = [False] * (n + 1)
            if dfs(u,-1):
                return [u,v]