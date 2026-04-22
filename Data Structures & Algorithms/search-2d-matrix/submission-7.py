class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        r = 0 
        while r < row:
            if matrix[r][0] <= target <= matrix[r][column-1]:
                left = 0
                right = column-1

                while left <= right:
                    m = (left+right) // 2
                    if matrix[r][m] == target:
                        return True
                    elif matrix[r][m] > target:
                        right = m - 1
                    else:
                        left = m + 1
                return False
            else:
                r += 1
        
        return False
