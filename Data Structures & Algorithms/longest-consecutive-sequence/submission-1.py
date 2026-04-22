class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        store = set(nums)
        ans = 0

        for num in nums:
            streak,curr = 0,num

            while curr in store:
                curr += 1
                streak += 1
            ans = max(ans,streak)
        
        return ans



