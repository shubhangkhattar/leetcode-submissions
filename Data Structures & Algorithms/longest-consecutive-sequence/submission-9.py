class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        max_result = 0

        for i in range(len(nums)):
            val = nums[i]
            count = 0
            while val in nums:
                count += 1
                val += 1
            max_result = max(count,max_result)

        return max_result