class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            house1, house2 = 0, 0

            for num in nums:
                house1, house2 = house2, max(house2,house1+num)

            return house2
        
        return max(helper(nums[1:]),helper(nums[:-1]),nums[0])