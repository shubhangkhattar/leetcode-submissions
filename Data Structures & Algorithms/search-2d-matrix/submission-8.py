class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROW = len(matrix)
        COL = len(matrix[0])

        l = 0 
        r = ROW*COL - 1

        while l <= r:
            m = (l + r) // 2
            row = m // COL 
            col = m % COL

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1
        
        return False



# row = m // COLS
# col = m % COLS

#    0   1   2   3
# 0  1   2   4   8 
# 1  10  11  12  13
# 2  14  20  30  40


# COL = 4

# 6 // 4
# 1

# 6 % 4 = 2


# 1 2 4 8 10 11 12 13 14 20 30 40
# 0 1 2 3 4  5  6  7  8  9  10 11
 

