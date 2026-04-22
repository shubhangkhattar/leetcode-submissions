class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        def dfs(i,total1,total2):
            if i == len(nums):
                return total1 == total2

            return dfs(i+1,nums[i]+total1,total2) or dfs(i+1,total1,total2+nums[i])
           
        return dfs(0,0,0)

            
