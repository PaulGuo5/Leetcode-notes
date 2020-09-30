class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        buy = prices[0]
        maxPro = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                if profit > maxPro:
                    maxPro = profit
        return maxPro
    
    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        res = 0
        min_ = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - min_ > 0:
                tmp = prices[i] - min_
                if tmp > res:
                    res = tmp
            if prices[i] < min_:
                min_ = prices[i]
        return res
            
        
    def maxProfit(self, prices: List[int]) -> int:    
        if not prices: return 0
        min_price = float("inf")
        res = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            res = max(res, prices[i] - min_price)
        return res