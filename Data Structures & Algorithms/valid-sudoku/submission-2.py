class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = defaultdict(list)
        vertical = defaultdict(list)
        box = defaultdict(list)

        def isValid(i,j):
            
            value = board[i][j]
            box_no = (j // 3) + (i//3)*3

            if value in horizontal[i] or value in vertical[j]  or value in box[box_no]:
                return False

            horizontal[i].append(value)                        
            vertical[j].append(value)
            box[box_no].append(value)

            return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "." and not isValid(i,j):
                    return False
        
        return True

  
        