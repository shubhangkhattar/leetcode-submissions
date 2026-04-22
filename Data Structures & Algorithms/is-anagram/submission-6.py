class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        countArray = [0] * 26
        
        for i in range(len(s)):
            countArray[ord(s[i]) - ord("a")] += 1
            countArray[ord(t[i]) - ord("a")] -= 1

        for val in countArray:
            if val != 0:
                return False
        
        return True