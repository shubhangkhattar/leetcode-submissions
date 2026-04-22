class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        low = 0
        high = 0 
        n = len(s)
        ans = 0

        while high < n:
            if s[high] not in my_set:
                my_set.add(s[high])
                ans = max(len(my_set),ans)
                high += 1
            else:
                my_set.remove(s[low])
                low += 1
        
        return ans