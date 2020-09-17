class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if not arr:
            return 0
        m, n = len(arr), len(arr[0])
        for i in range(1, m):
            for j in range(n):
                arr[i][j] = min([arr[i-1][col] for col in range(n) if col != j])+arr[i][j]
        
        return min(arr[-1])
