class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        def dfs(l,r):

            if l > r:
                return 0
            
            maxPoints = 0
            for i in range(l,r+1):
                points = nums[l-1] * nums[i] * nums[r+1]
                points += dfs(l,i-1) + dfs(i+1,r)
                maxPoints = max(maxPoints,points)
            return maxPoints
        
        return dfs(1,len(nums)-2)
