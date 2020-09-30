class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumList = 0
        for num in nums:
            sumList += num
        sumList2 = 0
        for i in range(len(nums)):
            if (sumList-nums[i])/2 == sumList2:
                return i
            sumList2 += nums[i]
        return -1