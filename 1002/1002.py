class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        pre = collections.Counter(A[0])
        for a in A:
            pre = (pre & collections.Counter(a))
        res = []
        for i, j in pre.items():
            while j >= 1:
                j-=1
                res.append(i)
        return res
