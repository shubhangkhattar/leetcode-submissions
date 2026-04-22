class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)

        memo = {}

        def dfs(i,j):
            
            if i == m or j == n:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            result = 0
            if text1[i] == text2[j]:
                result = dfs(i+1,j+1) + 1
                
            memo[(i,j)] = max(dfs(i+1,j),dfs(i,j+1),result)
            return memo[(i,j)]
        
        return dfs(0,0)