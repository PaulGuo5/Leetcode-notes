class Solution:
    def PredictTheWinner1(self, nums: List[int]) -> bool:
        self.m = [[float('inf')]*len(nums) for _ in range(len(nums))]
        def helper(nums, i, j):
            if i > j: return 0
            if i == j: return nums[i]
            if self.m[i][j] == float('inf'):
                self.m[i][j] = max(nums[i]-helper(nums, i+1, j), nums[j]-helper(nums, i, j-1))
            return self.m[i][j]
        return helper(nums, 0, len(nums)-1) >= 0
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for l in range(2, len(nums)+1):
            for i in range(len(nums)-l+1):
                j = i + l - 1
                dp[i][j] = max(nums[i]-dp[i+1][j], nums[j]-dp[i][j-1])
        return dp[0][-1] >= 0
