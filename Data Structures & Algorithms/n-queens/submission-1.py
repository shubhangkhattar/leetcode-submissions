class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        result = []
        def isItGood(r,c):
            i,j = r,c
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i,j = r,c
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            i,j = r,c
            while i >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1

            return True

        def dfs(i):

            if i >= n:
                result.append(["".join(row) for row in board])
                return
            
            for j in range(n):
                if isItGood(i,j):
                    board[i][j] = "Q"
                    dfs(i+1)
                    board[i][j] = "."

        
        dfs(0)
        return result
                    









