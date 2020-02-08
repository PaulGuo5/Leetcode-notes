class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        dp = [collections.defaultdict(int) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(len(nums)):
            for cur_sum, cnt in dp[i].items():
                dp[i+1][cur_sum-nums[i]] += cnt
                dp[i+1][cur_sum+nums[i]] += cnt
        return dp[-1][S]
