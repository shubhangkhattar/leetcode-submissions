class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        m = len(board)
        n = len(board[0])

        def dfs(i,j):
            if i in range(m) and j in range(n) and board[i][j] == "O":
                board[i][j] = "#"
                dfs(i-1,j)
                dfs(i+1,j)
                dfs(i,j-1)
                dfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if i in (0,m-1) or j in (0,n-1):
                    if board[i][j] == "O":
                        dfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    
                if board[i][j] == "#":
                    board[i][j] = "O"





