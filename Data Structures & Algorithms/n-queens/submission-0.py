class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."]*n for _ in range(n)]

        result = []

        def validate(board,row,col):
        
            
            #TOP-LEFT
            i,j = row,col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
                    
            
            # TOP-RIGHT
            i,j = row,col
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            # TOP
            i,j = row,col     
            while i >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
            return True


        def dfs(row,board):
            if row == n:
                result.append(["".join(board[i]) for i in range(n)])
                return 
            
            for col in range(n):
                if validate(board,row,col):
                    board[row][col] = "Q"
                    dfs(row+1,board)
                    board[row][col] = "."

        dfs(0,board)
        return result





