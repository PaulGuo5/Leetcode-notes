class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        count = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
                res = max(res, count)
            elif nums[i] <= nums[i-1]:
                count = 1
        return res