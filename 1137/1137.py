class Solution:
    def tribonacci1(self, n: int) -> int:
        # time limit exceeded
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
    
    
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        dp = [0 for i in range(n+1)]
        dp[1], dp[2] = 1, 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]
