class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        result = set()

        for word in words:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        if self.find(i,j,board,word,0,set()):
                            result.add(word)
        
        return list(result)


    def find(self,i,j,board,word,k,visit):
        if k == len(word):
            return True

        m = len(board)
        n = len(board[0])
        if 0 <= i < m and 0 <= j < n and (i,j) not in visit and board[i][j] == word[k]:
            visit.add((i,j))
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            for dr,dc in directions:
                row =  i + dr
                col =  j + dc
                if self.find(row,col,board,word,k+1,visit):
                    return True
            visit.remove((i,j))
        return False


    