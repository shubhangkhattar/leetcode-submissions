class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_water = 0

        left = 0
        right = len(height) - 1

        suffix = 0
        prefix = 0 

        while left <= right:
            
            prefix = max(height[left],prefix)
            suffix = max(height[right],suffix)

            if height[left] <= height[right]:
                max_water += max(min(prefix,suffix) - height[left],0)
                left += 1
            else:
                max_water += max(min(prefix,suffix) - height[right],0)
                right -= 1

        return max_water


        # [0,2,0,3,1,0,1,3,2,1]
