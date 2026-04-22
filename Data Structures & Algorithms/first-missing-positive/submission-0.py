class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1

        for num in nums:
            if num < missing:
                continue
            elif num > missing:
                return missing
            else:
                missing += 1
        
        return missing