class StockSpanner:

    def __init__(self):
        self.stock_stack = [] #pair (price,span)

    def next(self, price: int) -> int:
        span_length = 1
        while self.stock_stack and self.stock_stack[-1][0] <= price:
            span_length += self.stock_stack.pop()[1]
        
        self.stock_stack.append((price,span_length))

        return span_length


# [[], [100], [80], [60], [70], [60], [75], [85]]

#  100,1
#  80,1
#  75,4

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)