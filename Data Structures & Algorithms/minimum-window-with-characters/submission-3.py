from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hm_s = defaultdict(int)
        hm_t = defaultdict(int)

        for char in t:
            hm_t[char] += 1

        need = len(hm_t)
        have =0
        l = 0

        ans = ""

        for r in range(len(s)):
            hm_s[s[r]] += 1
            if s[r] in hm_t and hm_t[s[r]] == hm_s[s[r]]:
                have += 1
            
            while need == have:
                result = s[l:r+1]
                if len(result) < len(ans) or ans == "":
                    ans = result 
                if s[l] in hm_t:
                    hm_s[s[l]] -= 1
                    if hm_s[s[l]] < hm_t[s[l]]:
                        have -= 1
                l += 1

        return ans
   
        #     |   
        #              |
        # s="ADOBECODEBANC"
        # t="ABC"


        # result = "BANC"

        # need = 3
        # have = 3

        # t = {A:1,B:1,C:1}
        # s = {A:1,D:1,O:1,B:1,E:1,C:1}

