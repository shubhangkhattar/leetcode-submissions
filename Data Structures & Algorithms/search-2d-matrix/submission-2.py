class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                c -= 1
            else:
                r += 1
        
        return False
                

[[1,2,4,8],
[10,11,12,13],
[14,20,30,40]]