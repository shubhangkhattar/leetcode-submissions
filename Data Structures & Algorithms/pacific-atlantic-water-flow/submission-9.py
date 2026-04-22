class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()


        

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        
        def dfs(i,j,visited):
            
            visited.add((i,j))

            for dr,dc in directions:
                dr = i + dr
                dc = j +dc
                if (0 <= dr < m and
                    0 <= dc < n and
                    (dr,dc) not in visited
                    and heights[dr][dc] >= heights[i][j]
                    ):
                    dfs(dr,dc,visited)


        for i in range(m):
            dfs(i,0,pacific)
            dfs(i,n-1,atlantic)

        for j in range(n):
            dfs(0,j,pacific)
            dfs(m-1,j,atlantic)

        result = []
        for i,j in atlantic:
            if (i,j) in pacific:
                result.append([i,j])
        
        return result
