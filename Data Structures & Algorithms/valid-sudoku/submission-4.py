class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(list)
        cols = defaultdict(list)
        cells = defaultdict(list)

        def verify(row,col):
            val = board[row][col]
            
            if val in rows[row]:
                return False
            rows[row].append(val)
            
            if val in cols[col]:
                return False
            cols[col].append(val)

            cell = (col // 3) + (row // 3)*3
            if val in cells[cell]:
                return False
            cells[cell].append(val)

            return True

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != "." and not verify(i,j):
                    print(cells)
                    return False

        

        return True

        

