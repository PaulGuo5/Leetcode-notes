class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        n = len(nums)
        for i in range(n):
            while 0 <= nums[i]-1 < n and nums[nums[i]-1] != nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n + 1
