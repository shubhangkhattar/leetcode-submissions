class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj_matrix = defaultdict(list)

        for i,j in edges:
            adj_matrix[i].append(j)
            adj_matrix[j].append(i)
        
        path = set()
        def helper(node,prev):
            if node in path:
                return False
            
            path.add(node)
            
            for neighbor in adj_matrix[node]:
                if neighbor == prev:
                    continue
                if not helper(neighbor,node):
                    return False
            return True

        if not helper(0,None):
            return False
        print(path)
        return len(path) == n

