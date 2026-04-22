class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minArray = 100001
        total = 0
        left,right = 0,0

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minArray = min(minArray,right-left+1)
                total -= nums[left]
                left += 1

        return  0 if minArray == 100001 else minArray