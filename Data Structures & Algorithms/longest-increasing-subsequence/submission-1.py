class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)
        
        result = 1

        for i in range(len(dp)):
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1,dp[i])
            result = max(dp[i],result)

        return result

