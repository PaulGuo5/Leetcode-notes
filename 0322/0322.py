class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        max_ = float("inf")
        dp = [0] + [max_]*amount
        for i in range(1, amount+1):
            dp[i] = min([dp[i-c] if i-c >= 0 else max_ for c in coins]) + 1
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1
