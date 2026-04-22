from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        hashmap_row = defaultdict(set)
        hashmap_col = defaultdict(set)
        hashmap_square = defaultdict(set)

        for i in range(m):
            for j in range(n):
                e = board[i][j]
                if board[i][j] == ".":
                    continue
                row = i
                col = j
                square = (row//3*3)+col//3
                if e in hashmap_row[row] or e in hashmap_col[col] or e in hashmap_square[square]:
                    return False
                hashmap_row[row].add(e)
                hashmap_col[col].add(e)
                hashmap_square[square].add(e)

        return True

