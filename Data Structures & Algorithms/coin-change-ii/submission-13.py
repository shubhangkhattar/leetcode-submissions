class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        coins.sort()
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        
        for i in range(len(dp)):
            dp[i][0] = 1
        
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if coins[i-1] <= j:
                    dp[i][j] = dp[i][j-coins[i-1]]
                dp[i][j] += dp[i-1][j]
        return dp[-1][-1]






    #     0 1 2 3 4
    #   0 1 0 0 0 0
    #   1 1 1 1 1 1
    #   2 1 
    #   3 1 