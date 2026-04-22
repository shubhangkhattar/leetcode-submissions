class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(i,j):
            result = ""
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result = s[i:j+1]
                i -= 1   
                j += 1
            return result

        result = ""

        for i in range(len(s)):
            s1 = helper(i,i)
            s2 = helper(i,i+1)

            if len(s1) > len(result):
                result = s1
            
            if len(s2) > len(result):
                result = s2
        
        return result


                

            
