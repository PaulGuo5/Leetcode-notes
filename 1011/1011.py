class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left <= right:
            mid, cur, need = (left+right)//2, 0, 1
            for w in weights:
                if w + cur > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid - 1
        return left