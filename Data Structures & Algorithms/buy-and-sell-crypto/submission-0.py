class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            profit = price-min_price
            max_profit = max(profit,max_profit)
            min_price = min (min_price,price)
        
        return max_profit
    