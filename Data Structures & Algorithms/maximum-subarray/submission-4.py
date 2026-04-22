class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        running_sum = nums[0]
        for num in nums[1:]:
            running_sum = max(running_sum+num,num)
            max_sum = max(running_sum,max_sum)

        return max_sum
