class Solution:
    def divisorGame1(self, N: int) -> bool:
        return N % 2 == 0
    
    
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        for i in range(N+1):
            for j in range(1, i):
                if i%j == 0 and not dp[i-j]:
                    dp[i] = True
                    break
        return dp[-1]
