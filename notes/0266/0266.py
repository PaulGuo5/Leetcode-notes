class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = collections.Counter(s)
        flag = 1
        for i, j in cnt.items():
            if j % 2 != 0:
                flag -= 1
        return flag >= 0
