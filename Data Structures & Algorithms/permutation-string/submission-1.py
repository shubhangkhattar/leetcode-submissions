class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s1_set = sorted(list(s1))

        for i in range(n2):
            s2_set = list()
            j = i
            while j < n2 and j < i + n1:
                s2_set.append(s2[j])
                j += 1
            if sorted(s2_set) == s1_set:
                return True
        
        return False
                
