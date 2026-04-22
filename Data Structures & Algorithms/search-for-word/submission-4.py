class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        visited = set()

        def dfs(i,j,index):
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[index] and (i,j) not in visited:
                if index == len(word) - 1:
                    return True
                visited.add((i,j))
                if dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j-1,index+1) or dfs(i,j+1,index+1):
                    return True
                visited.remove((i,j))
            return False

        for i in range(m):
            for j in range(n):
                visited = set()
                if dfs(i,j,0):
                    return True
        
        return False