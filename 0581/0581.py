from collections import Counter
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_ = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < len(nums):
            if nums[i] != sorted_[i]:
                break
            i += 1
        while j >= 0:
            if nums[j] != sorted_[j]:
                break
            j -= 1
        return j - i + 1 if j > i else 0
