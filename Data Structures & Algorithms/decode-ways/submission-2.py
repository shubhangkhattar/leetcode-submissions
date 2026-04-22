class Solution:
    def numDecodings(self, s: str) -> int:
        

        def dfs(i):
            if i == len(s):
                return 1
            
            if s[i] == "0":
                return 0
            count = 0
            if i < len(s)-1 and 10 <= int(s[i:i+2]) <= 26:
                count = dfs(i+2)

            return dfs(i+1) + count

        return dfs(0)