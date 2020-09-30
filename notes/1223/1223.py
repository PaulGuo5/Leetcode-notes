class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        K = max(rollMax)
        dp = [[[0 for k in range(K)] for j in range(6)] for i in range(n)]
        for j in range(6): dp[0][j][0] = 1
        for i in range(1, n):
            for j in range(6):
                dp[i][j][0] += sum(dp[i-1][t][k] for t in range(6) for k in range(rollMax[t]) if t != j)
                for k in range(1, rollMax[j]):
                    dp[i][j][k] = dp[i-1][j][k-1]
        
        return sum(dp[n-1][j][k] for j in range(6) for k in range(K)) % (10**9+7)
