class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        for i in s:
            if i == "R":
                r += 1
            if i == "L":
                l += 1
            if l == r:
                l, r = 0, 0
                res += 1
        return res
