class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left, right = min(sweetness), sum(sweetness) // (K+1)
        while left <= right:
            mid = (left+right) // 2
            cur, cuts = 0, 0
            for s in sweetness:
                cur += s
                if cur > mid:
                    cur = 0
                    cuts += 1
            if cuts > K:
                left = mid + 1
            else:
                right = mid - 1 
        return left
