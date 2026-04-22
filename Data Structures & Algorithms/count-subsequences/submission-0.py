class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def dfs(i, j):
            if j == len(t):
                return 1

            count = 0
            for k in range(i, len(s)):
                if s[k] == t[j]:
                    count += dfs(k + 1, j + 1)

            return count

        return dfs(0, 0)
