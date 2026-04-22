class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        m = len(s1)
        n = len(s2)

        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[-1][-1] = True


        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i < n and s2[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True

                if j < m and s1[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]

#      0 1 2 3 4
#      a a a a - m(j)
# 0  b
# 1  b
# 2  b
# 3  b
# 4  -       T
#    n(i)


#   a a b b b b a a
#   0 1 2 3 4 5 6 7




