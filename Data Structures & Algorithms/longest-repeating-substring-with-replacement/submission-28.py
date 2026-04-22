from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        i = 0
        j = 0

        max_val = -1
        freq = defaultdict(int)

        while j < len(s):
            
            freq[s[j]] += 1
            
            if freq[s[j]] > max_val:
                max_val = freq[s[j]]
            
            if j - i - max_val >= k:
                freq[s[i]] -= 1
                i += 1

            result = max(result,j-i+1)

            j += 1

        return result

        # X 
        # Y
        
        
        
        #  AAABABB
        #  0123456
        #  i
        #   j
