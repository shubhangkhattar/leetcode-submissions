class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dfs(i,amount):

            
            if amount == 0:
                return 1
            
            if amount < 0 or i >= len(coins):
                return 0

            if (i,amount) in memo:
                return memo[(i,amount)]
            
            memo[(i,amount)] = dfs(i+1,amount) + dfs(i,amount-coins[i])
            return memo[(i,amount)]

        return dfs(0,amount)
        
    #   0 1 2 3 4 
    # - 1 0 0 0 0
    # 1 1 1 1 1 1  
    # 2 1 1 2 2 3
    # 3 1 1 2 3 4