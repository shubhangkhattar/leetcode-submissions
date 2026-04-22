class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        my_map = [[] for i in range(n)]

        for i,j in edges:
            my_map[i].append(j)
            my_map[j].append(i)

        traversal = set()
        def detect_back_edge(node,previous):
            
            nonlocal traversal
            
            traversal.add(node)
            for neighbor in my_map[node]:
                if neighbor == previous or neighbor in traversal:
                    continue
                detect_back_edge(neighbor,node)
            

        result = 0
        for i in range(n):
            if i not in traversal:
                result += 1
                detect_back_edge(i,-1)
        
        return result
            