class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                res = max(count,res)
                count = 0
        res = max(count,res)
        return res