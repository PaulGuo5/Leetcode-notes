class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k == 0:
            return 0
        n = len(prices)
        if n == 0:
            return 0
        if n == 1:
            if k == 1:
                return 0
            return prices[0]
        if k > n//2:
            max_ = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    max_ += prices[i]-prices[i-1]
            return max_
        else:
            dp = [[-float('inf')]*(2*k+2) for _ in range(n+1)]
            dp[0][1] = 0
            for i in range(1, n+1):
                # phase 1, 3, ..., 2*k+1
                for j in range(1, 2*k+2, 2):
                    dp[i][j] = dp[i-1][j]
                    if i-2 >= 0 and j-1 > 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j-1]+prices[i-1]-prices[i-2])
                # phase 2, 4, ..., 2*k
                for j in range(2, 2*k+1, 2):
                    dp[i][j] = dp[i-1][j-1]
                    if i-2 >= 0 and j-1 > 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j]+prices[i-1]-prices[i-2])
                        
            return max([dp[-1][j] for j in range(1, 2*k+2, 2)])
