class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        subsets = {-1: set()}
        for n in sorted(nums):
            subsets[n] = max([subsets[k] for k in subsets if n % k == 0], key = len)|{n}
        return list(max(subsets.values(), key=len))
