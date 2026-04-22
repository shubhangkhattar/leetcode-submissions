class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_map = defaultdict(int)
        max_count = 0
        max_value = None
        result = 0

        l = 0
        r = 0

        while r < len(s):
            
            my_map[s[r]] += 1

            if max_count < my_map[s[r]]:
                max_count = my_map[s[r]]
                max_value = s[r]

            if (r - l + 1) - max_count > k:
                my_map[s[l]] -= 1
                if max_value == s[l]:
                    max_count -= 1
                    for val,count in my_map.items():
                        if count > max_count:
                            max_value = val
                            max_count = count
                l += 1
            
            
            result = max(r - l + 1, result)
            r += 1
        
        return result




        