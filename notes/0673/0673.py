class Solution:
    def findNumberOfLIS1(self, nums: List[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))]
        longest = 1
        for i in range(len(nums)):
            cur_longest, cnt = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    cur_longest = max(cur_longest, dp[j][0]+1)
            for j in range(i):
                if cur_longest-1 == dp[j][0] and nums[j] < nums[i]:
                    cnt += dp[j][1]
            dp[i] = [cur_longest, max(dp[i][1], cnt)]
            longest = max(longest, cur_longest)
        return sum([item[1] for item in dp if item[0] == longest])
    
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1,1] for _ in range(len(nums))]
        longest = 1
        for i in range(len(nums)):
            cur_longest, cnt = 1, 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > cur_longest:
                        cur_longest = dp[j][0] + 1
                        cnt = 0
                    if dp[j][0] + 1 == cur_longest:
                        cnt += dp[j][1]
            dp[i] = [cur_longest, max(dp[i][1], cnt)]
            longest = max(longest, cur_longest)
        return sum([item[1] for item in dp if item[0] == longest])
