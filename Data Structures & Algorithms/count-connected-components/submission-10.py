class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_matrix = defaultdict(list)

        for i,j in edges:
            adj_matrix[i].append(j)
            adj_matrix[j].append(i)
        
        visited = set()
        
        def helper(node):
            if node in visited:
                return
        
            visited.add(node)
            
            for neighbor in adj_matrix[node]:
                if neighbor in visited:
                    continue
                helper(neighbor)
                  
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                helper(i)

        return count