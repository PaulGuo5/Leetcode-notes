class FenwickTree:
    def __init__(self, n):
        self.prefixSum = [0]*(n+1)
    def update(self, i, diff):
        while i < len(self.prefixSum):
            self.prefixSum[i] += diff
            i += i & -i
    def query(self, i):
        s = 0
        while i > 0:
            s += self.prefixSum[i]
            i -= i & -i
        return s
    
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ranks = collections.defaultdict(int)
        rank = 1
        for n in sorted(set(nums)):
            ranks[n] = rank
            rank += 1
        print(ranks)
        ft = FenwickTree(len(set(nums)))
        res = []
        for n in nums[::-1]:
            res.append(ft.query(ranks[n]))
            ft.update(ranks[n]+1, 1)
        return res[::-1]
