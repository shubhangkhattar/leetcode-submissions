class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW,COL = len(matrix),len(matrix[0])

        l = 0
        r = ROW * COL -1 

        while l <= r:
            m = l + (r-l)//2

            val = matrix[m//COL][m%COL]

            if val < target:
                l = m+1
            elif val > target:
                r = m-1
            else:
                return True
        
        return False


#         r*(C) + c = 8
        



#         0,1,2,3,4,5,6,7,8,9,10,11

# r = M // ROW


# R X C = 