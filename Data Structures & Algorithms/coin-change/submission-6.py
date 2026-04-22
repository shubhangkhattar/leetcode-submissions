class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf")]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(dp)):
            dp[i][0] = 0
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i][j-coins[i-1]] + 1
                dp[i][j] = min(dp[i][j],dp[i-1][j])
        
        return -1 if dp[-1][-1] == float("inf") else dp[-1][-1]

