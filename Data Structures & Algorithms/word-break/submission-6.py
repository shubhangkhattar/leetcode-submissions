class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        
        dp[0] = True

        for i in range(1,n+1):
            for word in wordDict:
                print(s[i-1:i+len(word)])
                if s[i-1:i+len(word)-1] == word and dp[i-1] == True:
                    dp[i+len(word)-1] = True
        return dp[-1]


        # - n e e t c o d e
        # 0 1 2 3 4 5 6 7 8
        # T


