class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        m = len(board)
        n = len(board[0])

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j,idx):
            if idx == len(word):
                return True
            if 0<=i<m and 0 <= j <n and word[idx] == board[i][j]:
                temp = board[i][j]
                board[i][j] = "#"
                for dr,dc in directions:
                    r = dr + i
                    c = dc + j
                    if dfs(r,c,idx+1):
                        return True
                board[i][j] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False


# [["A","B","C","E"],
#  ["S","F","C","S"],
#  ["A","D","E","E"]]