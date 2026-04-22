class Solution:
    def trap(self, height: List[int]) -> int:



        water = 0

        l = 0 
        r = len(height) - 1

        l_max = height[l]
        r_max = height[r]

        while l <= r:
            
            if l_max < r_max:
                water += l_max - height[l]
                l += 1
                l_max = max(l_max,height[l])
            else:
                water += r_max - height[r]
                r -= 1
                r_max = max(r_max,height[r])
            
        return water

