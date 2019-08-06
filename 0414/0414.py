class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        for i in range(2):
            nums.remove(max(nums))
        return max(nums)
