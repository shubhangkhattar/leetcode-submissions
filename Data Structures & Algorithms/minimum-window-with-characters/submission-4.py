class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_map = defaultdict(int)
        result = ""
        
       
        for char in t:
            t_map[char] += 1

        remaining = len(t_map)

        l = 0 
        r = 0

        while r < len(s):

            if s[r] in t_map:
                t_map[s[r]] -= 1
                if t_map[s[r]] == 0:
                    remaining -= 1
            


            while remaining == 0:
                if len(result) == 0 or r-l+1 < len(result):
                    result = s[l:r+1]
                if s[l] in t_map:
                    t_map[s[l]] += 1
                    if t_map[s[l]] == 1:
                        remaining += 1
                l += 1

            r += 1
            

        return result