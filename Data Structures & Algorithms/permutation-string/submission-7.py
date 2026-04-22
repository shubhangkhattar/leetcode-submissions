from collections import defaultdict,Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False
        
        freqMap = Counter(s1)

        right = 0
        left = 0

        while right < len(s2):
            if s2[right] in freqMap and freqMap[s2[right]] != 0:
                freqMap[s2[right]] -= 1
                right += 1
            else:
                freqMap[s2[left]] += 1
                left += 1

            if sum(freqMap.values()) == 0:
                return True

        return False            