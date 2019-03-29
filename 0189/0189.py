class Solution:
    def reverseList(self, nums, start, end):
        if start >= end:
            return nums
        ps = start
        pe = end
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1
        return nums
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length > 1:
            if length <= k:
                i = 0
                while i < k:
                    self.reverseList(nums, 0, length-1)
                    self.reverseList(nums, 1, length-1)
                    i += 1
            else:
                self.reverseList(nums, 0, length-1)
                self.reverseList(nums, 0, k-1)
                self.reverseList(nums, k, length-1)