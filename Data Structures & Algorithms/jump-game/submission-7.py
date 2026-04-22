class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        goal = n - 1
        dp = [False] * n
        dp[-1] = True

        for i in range(n-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
                dp[i] = True

        return dp[0]