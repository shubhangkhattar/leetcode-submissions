class StockSpanner:

    def __init__(self):
        self.stock_stack = []

    def next(self, price: int) -> int:
        span_length = 1
        temp_stock = []
        while self.stock_stack:
            if self.stock_stack[-1] <= price:
                temp_stock.append(self.stock_stack.pop())
                span_length += 1
            else:
                break
        while temp_stock:
            self.stock_stack.append(temp_stock.pop())
        
        self.stock_stack.append(price)
        return span_length

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)