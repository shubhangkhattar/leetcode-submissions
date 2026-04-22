class Solution:
    def longestPalindrome(self, s: str) -> str:

        def palindrome(left,right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        result = ""

        for i in range(len(s)):
            palindrome_1 = palindrome(i,i)
            palindrome_2 = palindrome(i,i+1)

            if len(palindrome_1) > len(result):
                result = palindrome_1
            if len(palindrome_2) > len(result):
                result = palindrome_2



        return result

