class Solution:
    def sortString(self, s: str) -> str:
        cnt = collections.Counter(s)
        l = 2*len(s)
        keys = sorted(cnt.keys())
        res = ""
        while l > 0:
            l -= 1
            for c in keys+keys[::-1]:
                if cnt[c] > 0:
                    cnt[c] -= 1
                    res+=c
        return res
