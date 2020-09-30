class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        res = 0
        for h in houses:
            # hi = bisect.bisect_left(heaters, h)
            hi = self.binarySearch(heaters, h)
            left = heaters[hi-1] if hi-1 >= 0 else -float('inf')
            right = heaters[hi] if hi < len(heaters) else float('inf')
            res = max(res, min(h-left, right-h))
        return res
    
    def binarySearch(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left
                
