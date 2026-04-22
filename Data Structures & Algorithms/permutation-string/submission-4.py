class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq_map = Counter(s1)
        copy_freq_map = freq_map.copy()

        left = 0
        right = 0 
        

        while right < len(s2):
            if s2[left] not in freq_map:
                left += 1
                right += 1
                continue 
            
            if s2[right] in freq_map and freq_map[s2[right]] != 0:
                freq_map[s2[right]] -= 1
                right += 1
            else:
                freq_map[s2[left]] += 1
                left += 1


            if sum(freq_map.values()) == 0:
                return True 

        return False


# Input: 

# s1 = "abc", 

# {a:1, b:1, c:1}

# s2 = "lecabee"
#       l
#        r
# Output: true