class Solution:
    def countSubstrings(self, s: str) -> int:
        
        result = 0

        def isPalindrome(l,r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
            return res

        ans = 0

        for i in range(len(s)):
            ans += isPalindrome(i,i)
            ans += isPalindrome(i,i+1)
            
        return ans

