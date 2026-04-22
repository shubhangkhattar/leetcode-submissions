class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hm_s = {}
        hm_t = {}

        for char in t:
            hm_t[char] = hm_t.get(char,0) + 1

        
        need = len(hm_t)
        have = 0

        l = 0
        ans = ""
        for r in range(len(s)):
            
            hm_s[s[r]] = hm_s.get(s[r],0) + 1
            if s[r] in hm_t and hm_s[s[r]] == hm_t.get(s[r],0):
                have += 1
 
            while need == have:
                sub_string = s[l:r+1]
                ans = sub_string if len(sub_string) < len(ans) or ans == "" else ans
                hm_s[s[l]] -= 1
                if s[l] in hm_t and hm_s[s[l]] < hm_t[s[l]]:
                    have -= 1
                l += 1
        
        return ans



            






            



            