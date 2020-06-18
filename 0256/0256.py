class Solution:
    def minCost1(self, costs: List[List[int]]) -> int:
        r, b, g = 0, 0, 0
        for rr, bb, gg in costs:
            r, b, g = min(b, g) + rr, min(r, g) + bb, min(r, b) + gg
        return min(r, b, g)
    
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        n = len(costs)
        r, b, g = [0]*n, [0]*n, [0]*n
        r[0], b[0], g[0] = costs[0][0], costs[0][1], costs[0][2]
        for i in range(1, n):
            r[i] = min(b[i-1], g[i-1]) + costs[i][0] 
            b[i] = min(r[i-1], g[i-1]) + costs[i][1]
            g[i] = min(b[i-1], r[i-1]) + costs[i][2]
        return min(r[-1], b[-1], g[-1])
