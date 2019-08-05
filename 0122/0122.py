class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        return sum(max(b-a,0)for a,b in zip(prices,prices[1:]))
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for a, b in zip(prices, prices[1:]):
            res.append(max(b-a, 0))
        return sum(res)
