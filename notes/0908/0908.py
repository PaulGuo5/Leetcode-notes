class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return 0 if ((max(A) - K) - (min(A) + K)) <= 0 else (max(A) - K) - (min(A) + K)
