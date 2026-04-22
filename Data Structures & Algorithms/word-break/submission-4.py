class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(1,len(dp)):
            for word in wordDict:
                if len(word) <= i:
                    if word == s[i-len(word):i] and dp[i-len(word)]:
                        dp[i] = True
        
        print (dp)

        return dp[-1]


        #   n e e t c o d e
        # T F F F F F F F F
        # 0 1 2 3 4 5 6 7 8
        #         i

        # n e e t c o d e
        # 0 1 2 3 4 5 6 7 


        # n e e t 
        # 0 1 2 3 

        # c o d e
        # 0 1 2 3  