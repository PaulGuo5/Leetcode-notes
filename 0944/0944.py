class Solution:
    def minDeletionSize1(self, A: List[str]) -> int:
        res = 0
        for i in zip(*A):
            if sorted(i) != list(i):
                res += 1
        return res
    
    def minDeletionSize2(self, A: List[str]) -> int:
        return sum(sorted(i) != list(i) for i in zip(*A))
    
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(any(a > b for a, b in zip(i, i[1:])) for i in zip(*A))
