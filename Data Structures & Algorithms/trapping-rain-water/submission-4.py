class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = 0
        prefix_list = [0]*len(height)

        suffix = 0
        suffix_list = [0]*len(height)

        for i in range(len(height)):
            prefix = max(prefix,height[i])
            prefix_list[i] = prefix

            suffix = max(suffix,height[len(height)-i-1])
            suffix_list[len(height)-i-1] = suffix
        
        max_water = 0
        for i in range(len(height)):
            cell_height = min(prefix_list[i],suffix_list[i])
            max_water  += max(cell_height-height[i],0)
        
        return max_water