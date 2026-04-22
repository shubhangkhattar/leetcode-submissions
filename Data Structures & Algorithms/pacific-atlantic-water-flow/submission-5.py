class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])
        
        pacific = set()
        atlantic = set()

        for i in range(m):
            self.dfs(i,0,heights,pacific)
            self.dfs(i,n-1,heights,atlantic)

        for j in range(n):
            self.dfs(0,j,heights,pacific)
            self.dfs(m-1,j,heights,atlantic)
        

        return list(pacific.intersection(atlantic))


    
    def dfs(self,i,j,heights,sea):

        sea.add((i,j))

        m = len(heights)
        n = len(heights[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for dr, dc in directions:
            row = i + dr
            col = j + dc
            if 0 <= row < m and 0 <= col < n and heights[i][j] <= heights[row][col] and (row,col) not in sea:
                self.dfs(row,col,heights,sea)
            