class Solution:
    def countSubstrings(self, s: str) -> int:
        

        def helper(i,j):
            
            count = 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                print(s[i:j+1])
                count += 1
                i -= 1
                j += 1
                
            return count
        
        result = 0
        for i in range(len(s)):
            result += helper(i,i)
            result += helper(i,i+1) 

        return result