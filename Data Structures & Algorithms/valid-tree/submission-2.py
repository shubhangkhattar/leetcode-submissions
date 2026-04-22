class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        my_map = [[] for i in range(n)]

        if len(edges) != n - 1:
            return False

        for i,j in edges:
            my_map[i].append(j)
            my_map[j].append(i)

        def dfs(node,visited,parent):
            
            if node in visited:
                return False
            
            if not my_map[node]:
                return True
            
            visited.add(node)
            
            for neighbor in my_map[node]:
                if neighbor != parent:
                    if not dfs(neighbor,visited,node):
                        return False
            return True


        
        return dfs(0,set(),-1)



        