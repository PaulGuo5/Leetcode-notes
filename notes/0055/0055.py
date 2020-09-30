class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        far = nums[0]
        for i in range(n):
            if i > far: break
            far = max(far, i + nums[i])
        return far >= n-1
    
    def canJumpDP(self, nums: List[int]) -> bool:
        dp = [True] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                dp[i] = dp[j] and nums[j] >= i-j
        return dp[-1]
