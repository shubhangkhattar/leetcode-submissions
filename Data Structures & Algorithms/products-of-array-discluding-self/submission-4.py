class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        result = [1]*len(nums)
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

            result[len(nums)-i-1] *= suffix
            suffix *= nums[len(nums)-i-1]

        return result
