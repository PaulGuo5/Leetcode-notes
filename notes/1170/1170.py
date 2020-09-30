class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        qq = [q.count(min(q)) for q in queries]
        ww = [w.count(min(w)) for w in words]
        ww.sort()
        # return [len(ww)-bisect.bisect_right(ww, q) for q in qq]
        return [len(ww)-self.minLarger(ww, q) for q in qq]
    
    def minLarger(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                if not mid-1 or nums[mid-1] < target:
                    return mid
                else:
                    right = mid - 1
        return left
