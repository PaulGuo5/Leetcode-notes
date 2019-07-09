class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        low, high = max(nums), sum(nums) + 1
        while low < high:
            mid = (low+high)//2
            if self.mid_groups(nums, mid) > m:
                low = mid + 1
            else:
                high = mid
        return low
    
    def mid_groups(self, nums, limit):
        cnt, groups = 0, 1
        for num in nums:
            if cnt + num > limit:
                cnt = num
                groups += 1
            else:
                cnt += num
        return groups
