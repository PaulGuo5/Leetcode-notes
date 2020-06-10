class Solution:
    def numRollsToTarget1(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target+1) for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for t in range(target+1):
                for j in range(1, min(t,f)+1):
                    dp[i][t] = (dp[i][t]+dp[i-1][t-j])%(10**9 + 7)
        return dp[d][target]
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0]*(target+1) for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, f+1):
                for t in range(j, target+1):
                    dp[i][t] = (dp[i][t]+dp[i-1][t-j])%(10**9 + 7)
        return dp[d][target]
