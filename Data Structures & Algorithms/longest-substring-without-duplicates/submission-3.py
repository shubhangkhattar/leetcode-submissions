class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        my_set = set()
        result = 0
        while right < len(s):
            if s[right] not in my_set:
                my_set.add(s[right])
                result = max(len(my_set),result)
                right += 1
            else:
                my_set.remove(s[left])
                left += 1
        return result
            