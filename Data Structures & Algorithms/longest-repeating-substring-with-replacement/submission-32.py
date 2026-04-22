class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        my_map = defaultdict(int)
        max_count = -1

        l = 0
        r = 0

        while r < len(s):
            
            
            my_map[s[r]] += 1

            if my_map[s[r]] > max_count:
                max_count = my_map[s[r]]
            
            if r-l+1 - max_count > k:
                my_map[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)
            r += 1

        return result

