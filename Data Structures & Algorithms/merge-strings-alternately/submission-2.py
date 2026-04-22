class Solution:
    def mergeAlternately(self, s1: str, s2: str) -> str:
        
        result = ""
        
        l = 0 
        r = 0


        while l < len(s1) and r < len(s2):
            result += s1[l] + s2[r]
            l += 1
            r += 1
        
        if l < len(s1):
            result += s1[l:]
        
        if r < len(s2):
            result += s2[r:]

        return result