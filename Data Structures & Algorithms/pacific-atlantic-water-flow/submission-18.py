class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        m = len(heights)
        n = len(heights[0])
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j,prev,curr_set):
            if i in range(m) and j in range(n) and (i,j) not in curr_set and heights[i][j] >= prev:
                curr_set.add((i,j))
                for dr,dc in directions:
                    r = dr + i
                    c = dc + j
                    dfs(r,c,heights[i][j],curr_set)
        
        for i in range(m):
            dfs(i,0,-1,pacific)
            dfs(i,n-1,-1,atlantic)
        
        for j in range(n):
            dfs(0,j,-1,pacific)
            dfs(m-1,j,-1,atlantic)

        return list(pacific.intersection(atlantic))

        




