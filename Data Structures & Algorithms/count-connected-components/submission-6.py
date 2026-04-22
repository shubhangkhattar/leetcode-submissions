class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_matrix = defaultdict(list)

        for i,j in edges:
            adj_matrix[i].append(j)
            adj_matrix[j].append(i)
        
        visited = set()

        def tree(vertice,prev):
                    
            if vertice in visited:
                return

            visited.add(vertice)
            for children in adj_matrix[vertice]:
                if children != prev:
                    tree(children,vertice)

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                tree(i,None)
        
        return count
