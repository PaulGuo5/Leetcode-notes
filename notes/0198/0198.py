            class Solution:
    def rob1(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0]*(n+1)
        dp[1] = nums[0]
        for i in range(2, n+1):
            dp[i] = max(nums[i-1]+dp[i-2], dp[i-1])
            
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        old, now = 0, nums[0]
        for i in range(2, n+1):
            tmp = max(nums[i-1]+old, now)
            old = now
            now = tmp
        return now
