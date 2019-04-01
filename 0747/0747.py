class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        max_index = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[max_index]:
                max_index = i
        for i in range(len(nums)):
            if i == max_index:
                continue
            if nums[i] * 2 > nums[max_index]:
                return -1
        return max_index