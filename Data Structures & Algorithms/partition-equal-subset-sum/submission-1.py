class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        def dfs(i,target):
            if i >= len(nums):
                if target == 0:
                    return True
                return False
            
            return dfs(i+1,target-nums[i]) or  dfs(i+1,target)
            
        return dfs(0,target)

