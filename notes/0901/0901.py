class StockSpanner:

    def __init__(self):
        self.stack = []
        
    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][1] <= price: 
            res += self.stack.pop()[0]
        self.stack.append((res, price))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
