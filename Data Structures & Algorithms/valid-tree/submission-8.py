class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_matrix = defaultdict(list)

        for i,j in edges:
            adj_matrix[i].append(j)
            adj_matrix[j].append(i)
        
        visited = set()

        def tree(vertice,prev):
                    
            if vertice in visited:
                return False

            visited.add(vertice)
            for children in adj_matrix[vertice]:
                if children != prev:
                    if not tree(children,vertice):
                        return False    
            return True
        if not tree(0,None):
            return False
        print(len(visited))
        print(n)
        return len(visited) == n

