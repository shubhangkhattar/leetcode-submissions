class Solution:
    def maxProfit(self, prices: List[int]) -> int:
         
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            profit = price-min_price
            min_price = min(min_price,price)
            max_profit = max(max_profit,profit)

        return max_profit
