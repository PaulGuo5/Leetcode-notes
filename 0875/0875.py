class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left+right)//2
            if sum((i+mid-1)//mid for i in piles) > H:
                left = mid + 1
            else:
                right = mid - 1
        return left
