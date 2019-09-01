class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        lo, hi, points, win = 0, 0, 0, 0
        for c in calories:
            win += c
            if hi - lo > k-1:
                win -= calories[lo]
                lo += 1
            if hi - lo == k-1:
                if win < lower:
                    points -= 1
                elif win > upper:
                    points += 1
            hi += 1
        return points
