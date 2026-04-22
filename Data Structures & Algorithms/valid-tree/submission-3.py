class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        my_map = [[] for i in range(n)]

        if len(edges) != n - 1:
            return False

        for i,j in edges:
            my_map[i].append(j)
            my_map[j].append(i)

        traversal = set()
        def detect_back_edge(node,previous):
            nonlocal traversal
            if node in traversal:
                return True
            
            traversal.add(node)
            for neighbor in my_map[node]:
                if neighbor == previous:
                    continue
                if detect_back_edge(neighbor,node):
                    return True
            
            return False

        return not detect_back_edge(0,-1)
        


