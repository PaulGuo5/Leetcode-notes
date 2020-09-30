class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def intWithBits(i):
            res = 0
            while i > 0:
                i, remain = divmod(i, 2)
                if remain == 1:
                    res += 1
            return res
        d = collections.defaultdict(list)
        for i in arr:
            d[intWithBits(i)].append(i)
        d_sorted = sorted(d.items(), key=lambda x: (x[0], x[1]))
        res = []
        for i, j in d_sorted:
            res += sorted(j)
        return res
