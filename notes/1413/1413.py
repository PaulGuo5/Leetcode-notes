class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        res = 1
        for n in nums:
            prefix_sum += n
            res = max(res, 1 - prefix_sum)
        return res
