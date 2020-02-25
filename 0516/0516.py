class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        
        for l in range(1, len(s)+1):
            for i in range(len(s)-l+1):
                j = i+l-1
                if i == j:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
