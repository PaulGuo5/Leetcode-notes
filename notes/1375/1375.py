class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        right, res = 0, 0
        for i, l in enumerate(light, 1):
            right = max(right, l)
            res += right == i
        return res
