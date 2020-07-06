class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            for j in range(k):
                costs[i][j] += min(costs[i-1][:j] + costs[i-1][j+1:])
        return min(costs[-1])
