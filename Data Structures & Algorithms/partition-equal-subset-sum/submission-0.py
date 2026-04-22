class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        subset1 = []
        subset2 = []

        def dfs(i):
            if i == len(nums):
                if sum(subset1) == sum(subset2):
                    return True
                return False
            
            subset1.append(nums[i])
            if dfs(i+1):
                return True
            subset1.pop()

            subset2.append(nums[i])
            if dfs(i+1):
                return True
            subset2.pop()

            return False
    
        return dfs(0)

