class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low+high) // 2
            start, cnt = 0, 0
            for i in range(len(nums)):
                while start < len(nums) and nums[i] - nums[start] > mid:
                    start += 1
                cnt += i - start
            if cnt < k:
                low = mid + 1
            else:
                high = mid
        return high
