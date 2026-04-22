class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])

        def dfs(pos,i,j,visited):

            if pos == len(word):
                return True
            
            if 0 <= i < m and 0 <= j < n and board[i][j] == word[pos] and (i,j) not in visited:
                dir = [(-1,0),(1,0),(0,-1),(0,1)]
                visited.append((i,j))
                for dr,dc in dir:
                    row = i + dr
                    col = j + dc
                    if dfs(pos+1,row,col,visited):
                        return True
                visited.pop()

            return False

        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and dfs(0,i,j,[]):
                    return True

        return False
        