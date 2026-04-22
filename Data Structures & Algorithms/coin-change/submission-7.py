class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    
        dp = [[float("inf")] * (amount+1) for _ in range(len(coins) + 1)]

        for i in range(len(dp)):
            dp[i][0] = 0

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i-1][j]
                if coins[i-1] <= j:
                    dp[i][j] = min(dp[i][j - coins[i-1]] + 1,dp[i][j]) 

        
        return -1 if dp[-1][-1] == float("inf") else dp[-1][-1]
     
     
     
        #    0 1 2 3 4 5 6 7 8 9 10 11 12
        # -  0 ! ! ! ! ! ! ! ! ! !   !  !
        # 1  0    
        # 5  0
        # 10 0