class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if num-1 in nums:
                continue
            count = 0
            while num in nums:
                num += 1
                count += 1
            result = max(result,count)
        return result