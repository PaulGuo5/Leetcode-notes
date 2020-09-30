class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def helper(nums):
            if not nums:
                return 0
            n = len(nums)
            if n == 1:
                return nums[0]
            
            old, now = 0, nums[0]
            for i in range(2, n+1):
                cur = max(old+nums[i-1], now)
                old = now
                now = cur
            return now
        
        return max(helper(nums[1:]), helper(nums[:-1]))
