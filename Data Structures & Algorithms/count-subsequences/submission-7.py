class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sn = len(s)
        tn = len(t)

        dp = [[0] * (sn+1) for _ in range(tn+1)]

        for j in range(len(dp[0])):
            dp[0][j] = 1



        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = dp[i][j-1]
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        
        for row in dp:
            print(row)

        return dp[-1][-1]



[1, 1, 1, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 1, 1, 1, 1]
[0, 0, 1, 1, 1, 1, 1, 1]
[0, 0, 0, 1, 2, 3, 3, 3]
[0, 0, 0, 1, 3, 6, 6, 6]
[0, 0, 0, 0, 0, 0, 6, 6]
[0, 0, 0, 0, 0, 0, 0, 6]