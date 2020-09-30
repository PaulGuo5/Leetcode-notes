class Solution:
    def checkRecord(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 3
        dp = [0]*(n+1)
        dp[0], dp[1], dp[2] = 1, 2, 4
        mod = 1000000007
        for i in range(3, n+1):
            dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%mod
        res = dp[n]
        for i in range(n):
            res += (dp[i]*dp[n-i-1])%mod
        res %= mod
        return res
