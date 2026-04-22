class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0 

        n = len(heights)

        left = 0
        right = n - 1

        while left < right:
            water = min(heights[left],heights[right])*(right-left)
            max_water = max(max_water,water)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water