class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        my_set = set()
        left = 0
        right = 0
        n = len(s)
        result = 0

        while right < n:
            if s[right] not in my_set:
                my_set.add(s[right])
                result = max(result,len(my_set))
                right += 1
            else:
                my_set.remove(s[left])
                left += 1

        return result
            
