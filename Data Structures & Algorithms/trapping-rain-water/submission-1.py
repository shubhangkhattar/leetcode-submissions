class Solution:
    def trap(self, nums: List[int]) -> int:
        
        n = len(nums)
        volume = 0
        prefix_list = [0]*n
        suffix_list = [0]*n

        prefix_max = 0 
        suffix_max = 0

        for i in range(n):
            prefix_max = max(prefix_max,nums[i])
            prefix_list[i] = prefix_max

            suffix_max = max(suffix_max,nums[n-i-1])
            suffix_list[n-i-1] = suffix_max

        
        for i in range(n):
            volume += max(0,min(prefix_list[i],suffix_list[i]) - nums[i])

        return volume


