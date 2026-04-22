class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        freq_map_1 = [0]*26
        freq_map_2 = [0]*26

        for i in range(len(s)):
            freq_map_1[ord(s[i])-ord('a')] += 1
            freq_map_2[ord(t[i])-ord('a')] += 1
        
        return freq_map_1 == freq_map_2


        