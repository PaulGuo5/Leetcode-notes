class Solution:
    def romanToInt(self, s: str) -> int:
        pre = None
        res = 0
        dict_ = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, None: 10000}
        for c in s:
            res += dict_[c] if dict_[pre] >= dict_[c] else dict_[c] - 2 * dict_[pre]
            pre = c
        return res
