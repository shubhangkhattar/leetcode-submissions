class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        min_price = prices[0]

        for price in prices:
            if price > min_price:
                profit += price - min_price
                min_price = price
            else:
                min_price = price
        
        return profit
        


        [7,1,5,3,6,4]
         