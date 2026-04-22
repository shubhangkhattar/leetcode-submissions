class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        n = len(nums)
        
        for i in range(n):
            pair = target - nums[i]
            
            if pair in my_map:
                return [my_map[pair],i]
            my_map[nums[i]] = i
        
        return []

