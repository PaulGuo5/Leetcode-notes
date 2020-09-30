class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(n < 0 for row in grid for n in row)
