class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        hor = sum(map(max, grid))
        ver = sum(map(max,zip(*grid)))
        top = sum(v > 0 for row in grid for v in row)
        return hor + ver + top
