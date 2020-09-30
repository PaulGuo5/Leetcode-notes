class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        n = len(nums)
        
        def first():
            left, right = 0, n-1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1 if left == n or nums[left] != target else left
        
        def last():
            left, right = 0, n-1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            left -= 1
            return -1 if left < 0 or nums[left] != target else left
        
        return [first(), last()]
