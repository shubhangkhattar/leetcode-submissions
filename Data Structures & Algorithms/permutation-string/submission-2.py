class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        set_1 = sorted(s1)
        
        set_2 = []
        for high in range(n2):
            set_2.append(s2[high])
            if sorted(set_2) == sorted(set_1):
                return True
            if len(set_1) == len(set_2):
                set_2.pop(0)

        return False