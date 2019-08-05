class Solution:
    def rob1(self, nums: List[int]) -> int:
        #dp
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]
    
    def rob(self, nums: List[int]) -> int:
        pre, cur = 0, 0
        for n in nums:
            tmp = pre #i-2
            pre = cur #i-1
            cur = max(n + tmp, pre)
            # cur, pre = max(n+pre, cur), cur
        return cur
            
