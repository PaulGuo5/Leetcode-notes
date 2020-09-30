class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        left, right = 0, 0
        s = 1
        res = 0
        while right < len(nums):
            s *= nums[right]
            if s >= k:
                while s >= k and left <= right:
                    s /= nums[left]
                    left += 1
            res += right - left + 1
            right += 1
        return res
