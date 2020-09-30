class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(n):
            if dp[0][i-1] and p[i] == "*":
                dp[0][i+1] = True
        for i in range(m):
            for j in range(n):
                if s[i] == p[j]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == ".":
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == "*":
                    if p[j-1] != s[i] and p[j-1] != ".":
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = (dp[i+1][j] or dp[i][j+1] or dp[i+1][j-1])
        return dp[-1][-1]
                        
