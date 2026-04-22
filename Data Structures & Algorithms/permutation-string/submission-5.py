class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        s1_map = Counter(s1)
        window_map = Counter(s2[:len(s1)])

        if s1_map == window_map:
            return True
        
        for i in range(len_s1,len_s2):
            
            window_map[s2[i]] += 1
            window_map[s2[i-len_s1]] -= 1

            if window_map[s2[i-len_s1]] == 0:
                del window_map[s2[i-len_s1]]

            if s1_map == window_map:
                return True 

        return False