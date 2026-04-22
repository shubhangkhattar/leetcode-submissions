class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()

        low = 0
        high = 0
        ans = 0
        while high < len(s):
            
            if s[high] not in my_set:
                my_set.add(s[high])
                ans = max(ans,len(my_set))
                high += 1
            else:
                my_set.remove(s[low])
                low += 1

            

        return ans
            