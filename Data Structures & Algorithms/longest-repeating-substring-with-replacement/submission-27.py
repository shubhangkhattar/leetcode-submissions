class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        
        left = 0
        right = 0

        max_val = -1

        freq_map = defaultdict(int)

        while right < len(s):
            
            freq_map[s[right]] += 1
            if freq_map[s[right]] > max_val:
                max_val = freq_map[s[right]]

            if (right - left - max_val + 1) > k:
                freq_map[s[left]] -= 1
                left += 1



            result = max(result,right - left+1)

            right += 1

        return result

# Input: s = "AAABABB", k = 1
#             L
#             R

# Output: 5


