class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0]*26
        s2_map = [0]*26

        for char in s1:
            s1_map[ord(char)- ord('a')] += 1
        
        l = 0
        r = 0

        while r < len(s2):

            s2_map[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 > len(s1):
                s2_map[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if s1_map == s2_map:
                return True
            
            r += 1
        
        return False