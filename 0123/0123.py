class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[-float('inf')]*(6) for _ in range(n+1)]
        dp[0][1] = 0
        
        for i in range(1, n+1):
            # phase 1, 3, 5
            for j in range(1, 6, 2):
                dp[i][j] = dp[i-1][j]
                if j-1 > 0 and i >= 2:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1]+prices[i-1]-prices[i-2])
                    
            # phase 2, 4
            for j in range(2, 5, 2):
                dp[i][j] = dp[i-1][j-1]
                if i-2 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j]+prices[i-1]-prices[i-2])
        
        return max(dp[-1][1], dp[-1][3], dp[-1][5])
