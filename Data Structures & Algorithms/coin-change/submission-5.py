class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}


        def dfs(i,target):

            if (i,target) in memo:
                return memo[(i,target)]

            if target == 0:
                return 0

            if target < 0 or i >= len(coins):
                return float("inf")
            

            memo[(i,target)] = min(dfs(i+1,target),dfs(i,target-coins[i])+1)
            
            return memo[(i,target)]

        result = dfs(0,amount)
        return result if result != float("inf") else -1

