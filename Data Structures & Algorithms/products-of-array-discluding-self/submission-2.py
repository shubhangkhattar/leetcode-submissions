class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        n = len(nums)
        result = [1]*n
        
        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

            result[n-i-1] *= postfix
            postfix *= nums[n-i-1]

            result[i]

        return result

