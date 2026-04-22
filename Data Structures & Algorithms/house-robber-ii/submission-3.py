class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            rob_1, rob_2 = 0,0
            for house in nums:
                temp = max(rob_1 + house, rob_2)
                rob_1 = rob_2
                rob_2 = temp
            return rob_2

        return max(nums[0], helper(nums[:-1]), helper(nums[1:]))