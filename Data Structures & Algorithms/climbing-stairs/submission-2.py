class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * n


        def dfs(stair):
            if stair == n:
                return 1
            if stair > n:
                return 0
            
            if cache[stair] != -1:
                return cache[stair]

            cache[stair] = dfs(stair+1) + dfs(stair+2)
            return cache[stair]
        
        dfs(0)

        return cache[0]
