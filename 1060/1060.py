class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid]-nums[0]-mid < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return nums[0]+k+lo-1
