class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        result = []
        for i in range(m):
            for j in range(n):
                if self.pacific(i,j,heights,set()) and self.atlantic(i,j,heights,set()):
                    result.append([i,j])

        return result

    
    def pacific(self, i, j, heights,visit):
        visit.add((i,j))
        if i == 0 or j == 0:
            return True
        
        m = len(heights)
        n = len(heights[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            row = i + dr
            col = j + dc
            if 0 <= row < m and 0 <= col < n and (row,col) not in visit and heights[row][col] <= heights[i][j] :
                if self.pacific(row,col,heights,visit):
                    return True
        visit.remove((i,j))
        return False

    def atlantic(self, i, j, heights,visit):    
        visit.add((i,j))    
        m = len(heights)
        n = len(heights[0])

        if i == m-1 or j == n-1:
            return True

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for dr,dc in directions:
            row = i + dr
            col = j + dc
            if 0 <= row < m and 0 <= col < n and (row,col) not in visit and heights[row][col] <= heights[i][j] :
                if self.atlantic(row,col,heights,visit):
                    return True
        visit.remove((i,j))
        return False
    