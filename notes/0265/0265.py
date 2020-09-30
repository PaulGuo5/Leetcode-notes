class Solution:
    def minCostII1(self, costs: List[List[int]]) -> int:
        # O(nk**2)
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            for j in range(k):
                costs[i][j] += min(costs[i-1][:j] + costs[i-1][j+1:])
        return min(costs[-1])
    
    def minCostII(self, costs: List[List[int]]) -> int:
        O(nk)
        if not costs: return 0
        n, k = len(costs), len(costs[0])
            
        for i in range(1, n):
            min1, min2 = float('inf'), float('inf')
            idx1, idx2 = 0, 0
            for j in range(k):
                cur = costs[i-1][j]
                if cur < min1:
                    min2 = min1
                    min1 = cur
                    idx2 = idx1
                    idx1 = j
                else:
                    if cur < min2:
                        min2 = cur
                        idx2 = j
            for j in range(k):
                if j != idx1:
                    costs[i][j] += min1
                else:
                    costs[i][j] += min2
        return min(costs[-1])
