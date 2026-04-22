class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1,n + 1):
            for a in range(amount + 1):
                print(i)
                dp[i][a] = dp[i - 1][a]
                dp[i][a] += dp[i][a - coins[i-1]] if a - coins[i-1] >=0 else 0
                
        return dp[n][amount]