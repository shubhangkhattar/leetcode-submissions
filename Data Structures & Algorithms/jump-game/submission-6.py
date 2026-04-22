class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True
        for i in range(len(nums)-2,-1,-1):
            end = min(i+nums[i]+1,len(nums))
            for j in range(i,end):
                if dp[j] == True:
                    dp[i] = True
                    break

        return dp[0]