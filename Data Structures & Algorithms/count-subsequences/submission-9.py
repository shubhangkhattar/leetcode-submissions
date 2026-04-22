class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dp = [[0] * (len(s)+1) for _ in range(len(t)+1)]

        dp[0] = [1]*(len(s)+1)

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i][j-1]
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[-1][-1]




    #     - c a a a t
    #   - 1 1 1 1 1 1
    #   c 0 1 1 1 1 1
    #   a 0 0 1 2 3 3
    #   t 0 0 0 0 0 3


