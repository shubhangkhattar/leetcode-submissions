class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_map = {}

        for i in range(len(nums)):
            key = target-nums[i]
            if key in my_map:
                return [my_map[key],i]
            my_map[nums[i]] = i