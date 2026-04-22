class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        prefix_list = [1]*len(nums)
        suffix_list = [1]*len(nums)
        result = [1]*len(nums)
        for i in range(len(nums)):
            prefix_list[i] = prefix
            prefix *= nums[i]

            suffix_list[len(nums)-i-1] = suffix
            suffix *= nums[len(nums)-i-1]

        for i in range(len(nums)):
            result[i] = prefix_list[i] * suffix_list[i]

        return result
