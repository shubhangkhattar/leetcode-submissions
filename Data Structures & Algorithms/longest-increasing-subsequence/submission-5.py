class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        max_count = 1
        n = len(nums)

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],1+dp[j])
            max_count = max(dp[i],max_count)
                
        return max_count