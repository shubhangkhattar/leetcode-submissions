class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            area = min(heights[left],heights[right]) * (right - left)
            print(left," ",right)
            max_area = max(max_area,area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
        
        
        #   0.1 2 3 4. 5. 6. 7.  8 9 10 11. 12. 13
#        [1,7,2,5,12,3,500,500,7,8,4, 7,  3,  6]
#                         L
#                             R
# 72


# 
# 
# 
# 
# 


