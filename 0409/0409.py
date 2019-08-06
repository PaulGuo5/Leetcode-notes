from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt_s = Counter(s)
        res = 0
        flag = False
        for i, j in cnt_s.items():
            if j % 2 == 0:
                res += j
            else:
                if flag:
                    res += j-1
                else:
                    flag = True
                    res += j
        return res
