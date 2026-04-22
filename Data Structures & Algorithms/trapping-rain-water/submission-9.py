class Solution:
    def trap(self, height: List[int]) -> int:
        l_arr = [0]*len(height)
        r_arr = [0]*len(height)

        l_max = 0
        r_max = 0

        for i in range(len(height)):
            
            l_max = max(l_max,height[i])
            r_max = max(r_max,height[len(height)-i-1])

            l_arr[i] = l_max
            r_arr[len(height)-i-1] = r_max

        water = 0
        
        for i in range(len(height)):
            water += max(min(l_arr[i],r_arr[i]) - height[i],0)

        return water

