class Solution:
    def countSubstrings(self, s: str) -> int:

        ans = 0
        
        def palindrome(left,right):

            res = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1

            return res

        result = ""

        for i in range(len(s)):
                ans += palindrome(i,i)
                ans += palindrome(i,i+1)
            
        return ans      