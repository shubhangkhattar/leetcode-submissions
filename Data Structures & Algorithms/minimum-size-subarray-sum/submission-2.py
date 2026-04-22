class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0
        r = 0

        result = len(nums) + 1
        total = 0

        while r < len(nums):
            total += nums[r]
            while total >= target:
                result = min(result,r-l+1)
                total -= nums[l]
                l += 1
            r += 1
        
        return 0 if result == len(nums) + 1 else result  

