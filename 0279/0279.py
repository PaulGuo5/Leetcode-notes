class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-j*j]+1)
        return dp[-1]
