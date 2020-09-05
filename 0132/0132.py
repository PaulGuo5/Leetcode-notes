class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(i):
                if s[j:i][::-1] == s[j:i]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]-1
