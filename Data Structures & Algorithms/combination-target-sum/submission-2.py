class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        result = []

        def dfs(i,subset,total):
            if total == 0:
                result.append(subset[:])
                return
            if total < 0 or i >= len(nums):
                return
            subset.append(nums[i])
            dfs(i,subset,total-nums[i]) 
            subset.pop()
            dfs(i+1,subset,total) 
        dfs(0,[],target)
        return result
