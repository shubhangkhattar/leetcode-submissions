class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        result =  1
        n = len(nums)

        for i in range(n):
            for j in range(i,-1,-1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
            result = max(dp[i],result)

        return result
