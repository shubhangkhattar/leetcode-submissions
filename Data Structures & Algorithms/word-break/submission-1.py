class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        n = len(s)
        
        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n-1,-1,-1):
            for word in wordDict:
                if not i + len(word) > n:
                    if s[i:i+len(word)] == word and dp[i+len(word)] == True:
                        dp[i] = True
                        break
        
        return dp[0]


