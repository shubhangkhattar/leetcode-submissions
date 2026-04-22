class Solution:
    def climbStairs(self, n: int) -> int:
        
        def dfs(stair):
            if stair == n:
                return 1
            if stair > n:
                return 0
            return dfs(stair+1) + dfs(stair+2)
        
        return dfs(0)
