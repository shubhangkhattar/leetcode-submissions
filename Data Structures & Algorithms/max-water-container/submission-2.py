class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_water = 0
        n = len(heights)
        left = 0 
        right = n - 1

        while left < right:
             
            height = min(heights[left],heights[right])
            width = right - left
             
            max_water = max(height*width,max_water)

            if(heights[left] > heights[right]):
                right -= 1
            else:
                left += 1
        
        return max_water