class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1 = 0
        s2 = 0
        result = ""

        while s1 < len(word1) and s2 < len(word2):
            result += (word1[s1] + word2[s2])
            s1 += 1
            s2 += 1
        
        if s1 < len(word1):
            return result + word1[s1:]
        
        if s2 < len(word2):
            return result + word2[s2:]
            
        return result