class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            if len(nums) == 1:
                return nums[0]

            if len(nums) == 0:
                return 0

            h1 = 0
            h2 = nums[0]

            for num in nums[1:]:
                h1,h2 = h2,max((h1+num),h2)
            return h2

        return max(helper(nums[:-1]),helper(nums[1:]))