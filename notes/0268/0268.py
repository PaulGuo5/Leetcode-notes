class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for num in range(len(nums)):
            if num == nums[-1]:
                return num+1
            if num != nums[num]:
                return num