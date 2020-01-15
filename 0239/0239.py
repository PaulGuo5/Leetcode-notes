class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        dp = [-float('inf')]*(len(nums)-k+1)
        dp[0] = max(nums[:k])
        for i in range(1, len(dp)):
            if nums[i+k-1] > dp[i-1]:
                dp[i] = nums[i+k-1]
            if nums[i+k-1] < dp[i-1] and nums[i-1] < dp[i-1]:
                dp[i] = dp[i-1]
            else:
                dp[i] = max(nums[i:i+k])
        return dp
