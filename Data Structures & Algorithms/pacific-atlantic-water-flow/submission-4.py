class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        result = []
        for i in range(m):
            for j in range(n):
                pacific,atlantic =  self.dfs(i,j,heights,set(),False,False)
                if pacific and atlantic:
                    result.append([i,j])

        return result


    def dfs(self, i, j, heights,visit, pacific, atlantic):    
        visit.add((i,j))    
        m = len(heights)
        n = len(heights[0])

        if i == m-1 or j == n-1:
            pacific = True
        
        if i == 0 or j == 0:
            atlantic = True

        if pacific and atlantic:
            return (pacific,atlantic)

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            row = i + dr
            col = j + dc
            if 0 <= row < m and 0 <= col < n and (row,col) not in visit and heights[row][col] <= heights[i][j] :
                pacific,atlantic = self.dfs(row,col,heights,visit, pacific, atlantic)
        visit.remove((i,j))
        return (pacific,atlantic)
    