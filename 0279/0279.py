class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i*i for i in range(int(n**0.5)+1)]
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for square_num in square_nums:
                if i < square_num: break
                dp[i] = min(dp[i], dp[i-square_num]+1)
        return dp[-1]
