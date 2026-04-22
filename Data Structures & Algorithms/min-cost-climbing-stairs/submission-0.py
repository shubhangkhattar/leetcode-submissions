class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        # dp = [-1]*n

        def dfs(stair,current_cost):
            if stair >= n:
                return current_cost
            
            # if dp[stair] != -1:
            #     return dp[stair]
            
            current_cost += cost[stair]
            
            current_stair_cost = min(dfs(stair+1,current_cost),dfs(stair+2,current_cost))
            # dp[stair] = current_stair_cost

            return current_stair_cost

        return min(dfs(0,0),dfs(1,0))




