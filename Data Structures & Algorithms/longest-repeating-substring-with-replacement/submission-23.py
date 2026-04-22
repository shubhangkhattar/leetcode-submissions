import heapq

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = {}
        
        left = 0
        ans = 0

        for right in range(n):
            
            count[s[right]] = count.get(s[right],0) + 1
            if (right-left+1) - max(count.values()) <= k:
                ans = max(ans,(right-left+1))
            else:
                count[s[left]] -= 1
                left += 1
        
        return ans
