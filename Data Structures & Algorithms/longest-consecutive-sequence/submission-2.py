class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        store = set(nums)
        ans = 0

        for num in nums:
            streak,curr = 0,num

            if curr-1 not in store:
                while curr in store:
                    streak += 1
                    curr += 1
                
            ans = max(ans,streak)
        
        return ans



