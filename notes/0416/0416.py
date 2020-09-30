class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, s = len(nums), sum(nums)
        if n <= 1 or s % 2 != 0: return False
        s //= 2
        dp = [[False]*(s+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
            
        for i in range(n):
            for j in range(s):
                dp[i+1][j+1] = dp[i][j+1]
                if nums[i] <= j+1:
                    dp[i+1][j+1] = dp[i+1][j+1] or dp[i][j+1-nums[i]]
        return dp[-1][-1]
