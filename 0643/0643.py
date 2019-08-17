class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        tmp_sum = sum(nums[:k])
        for i in range(1, len(nums)-k+1):
            tmp_sum = tmp_sum-nums[i-1]+nums[i+k-1]
            max_sum = max(max_sum, tmp_sum)
        return max_sum/k
