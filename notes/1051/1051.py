class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        right = sorted(heights)
        for i, j in zip(heights, right):
            if i != j:
                res += 1
        return res
