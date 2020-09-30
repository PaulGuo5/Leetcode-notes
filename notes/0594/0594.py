class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        l = 0
        for i, j in c.items():
            if i+1 in c:
                l = max(l, j+c[i+1])
            if i-1 in c:
                l = max(l, j+c[i-1])
        return l
