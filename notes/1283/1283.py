class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            mid = (left+right)//2
            if sum((i+mid-1)//mid for i in nums) > threshold:
                left = mid + 1
            else: right = mid - 1
        return left
