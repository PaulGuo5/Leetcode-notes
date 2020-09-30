class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def getGroup(nums, mid):
            cnt, group = 0, 1
            for num in nums:
                if cnt + num > mid:
                    group += 1
                    cnt = num
                else:
                    cnt += num
            return group
        
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low+high) // 2
            if getGroup(nums, mid) > m:
                low = mid + 1
            else:
                high = mid
        return low