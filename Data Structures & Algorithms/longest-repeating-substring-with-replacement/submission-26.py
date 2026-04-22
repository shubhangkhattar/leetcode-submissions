class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        
        result = 0
        
        count = {}

        max_freq = 0

        left = 0
        right = 0

        while right < n:
            
            count[s[right]] = count.get(s[right],0) + 1
            
            max_freq = max(max_freq,count[s[right]])

            while (right - left + 1 - max_freq) > k:
                count[s[left]] -= 1
                left += 1

            result = max(right - left + 1,result)

            right += 1
        return result








