class Solution:
    def findPeakElement1(self, nums: List[int]) -> int:
        if len(nums) == 1 or 0:
            return 0
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            return 1
        pre = nums[0]
        for i in range(1, len(nums)-1):
            if pre < nums[i] and nums[i] > nums[i+1]:
                return i
            else:
                pre = nums[i]
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        return 0

    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        return low
