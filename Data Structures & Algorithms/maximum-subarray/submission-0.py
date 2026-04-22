class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ans = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            max_sum = max(max_sum+num,num)
            max_ans = max(max_ans,max_sum)
        return max_ans