class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj = [[] for _ in range(n)]
        visited = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        

        def dfs(node):
            
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        result = 0

        for i in range(n):
            if not visited[i]:
                result += 1
                dfs(i)
        
        return result

