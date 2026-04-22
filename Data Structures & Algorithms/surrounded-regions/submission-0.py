class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(i,j):
            if 0 <= i < ROWS and 0 <= j < COLS and board[i][j] == "O":
                board[i][j] = "#"
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i,j+1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if (
                    i == 0 or 
                    i == ROWS - 1 or 
                    j == 0 or 
                    j == COLS - 1
                    ) and board[i][j] == "O":
                    dfs(i,j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "#":
                    board[i][j] = "O"

                    
