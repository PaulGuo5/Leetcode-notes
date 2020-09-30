class Solution:
    def change1(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for j in range(1, amount+1):
                dp[i][j] = dp[i-1][j] + dp[i][j - coins[i - 1]] if j >= coins[i - 1] else dp[i-1][j]
        return dp[-1][-1]
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[-1]
