class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        l, r = min(a, b, c), max(a, b, c)
        m = a + b + c - l - r
        if r - l == 2:
            return [0, 0]
        if r - m <= 2 or m - l <= 2:
            return [1, r - l - 2]
        else:
            return [2, r - l - 2]
