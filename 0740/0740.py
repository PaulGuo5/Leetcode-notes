class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        min_, max_ = float('inf'), -float('inf')
        d = collections.defaultdict(int)
        for n in nums:
            d[n] += 1
            min_ = min(min_, n)
            max_ = max(max_, n)
        pre, cur = 0, 0
        for i in range(min_, max_+1):
            pre, cur = cur, max(cur, d[i]*i+pre)
        return cur
