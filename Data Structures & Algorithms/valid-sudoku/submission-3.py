from collections import defaultdict

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = defaultdict(list)
        col = defaultdict(list)
        box_dict = defaultdict(list)

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                
                if value != ".":
                    
                    if value in row[i]:
                        return False
                    row[i].append(board[i][j])
                    
                    if value in col[j]:
                        return False
                    col[j].append(board[i][j])

                    box = (j//3) + (i//3)*3

                    if value in box_dict[box]:
                        return False
                    
                    box_dict[box].append(board[i][j])


        return True

        