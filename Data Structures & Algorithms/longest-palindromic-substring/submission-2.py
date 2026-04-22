class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(l,r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1 
                r += 1
            return s[l+1:r]

        result = ""
        
        for i in range(len(s)):
            result1 = helper(i,i)
            result2 = helper(i,i+1) if i < len(s)-1 else ""

            if len(result) < len(result1):
                result = result1

            if len(result) < len(result2):
                result = result2
        
        return result