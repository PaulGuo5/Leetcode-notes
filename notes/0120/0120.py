class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                tmp = float('inf')
                if 0 <= j < len(triangle[i-1]):
                    tmp = min(tmp,triangle[i-1][j])
                if 0 <= j-1 < len(triangle[i-1]):
                    tmp = min(tmp,triangle[i-1][j-1])
                triangle[i][j] += tmp
        return min(triangle[-1])
