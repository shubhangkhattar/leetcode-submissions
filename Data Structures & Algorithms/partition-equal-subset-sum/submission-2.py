class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        memo = [False] * len(nums)

        def dfs(i,target):
            if i >= len(nums):
                if target == 0:
                    return True
                return False
            
            if memo[i]:
                return True
            
            memo[i] = dfs(i+1,target-nums[i]) or  dfs(i+1,target)
            return memo[i]
            
        return dfs(0,target)

