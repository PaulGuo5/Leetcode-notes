class Solution:
    def superEggDrop1(self, K: int, N: int) -> int:
        #TLE
        dp=[[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N+1):
            dp[1][j] = j
        
        for i in range(2, K+1):
            for j in range(2, N+1):
                for k in range(1, j+1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][k-1], dp[i][j-k]))
        return dp[K][N]
    
    def superEggDrop(self, K: int, N: int) -> int:
        dp=[[float('inf')]*(N+1) for _ in range(K+1)]
        for i in range(1, K+1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N+1):
            dp[1][j] = j
            
        for i in range(2, K+1):
            k = 1
            for j in range(2, N+1):
                while k < j+1 and dp[i][j-k] > dp[i-1][k-1]:
                    k += 1
                dp[i][j] = 1 + dp[i-1][k-1]
        return dp[K][N]
