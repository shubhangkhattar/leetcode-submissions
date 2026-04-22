class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        rep_1 = [0]*26
        rep_2 = [0]*26


        for char in s:
            rep_1[ord(char)-ord('a')] += 1
        for char in t:
            rep_2[ord(char)-ord('a')] += 1
        return rep_1 == rep_2