class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[-1]*max(nums[0]*nums[1], nums[-2]*nums[-3])
