class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        last = 1#position of the last unique element
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[last] = nums[i]
                last += 1
        return last